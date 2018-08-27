"""
Usage:
  python main.py parse_athlete_events
  python main.py query_azure_olympics_db
  python main.py query_azure_olympics_db_orm
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import csv
import json
import os
import sys
import time
import traceback

import psycopg2

# see http://initd.org/psycopg/docs/
# https://docs.microsoft.com/en-us/azure/postgresql/connect-python

from datetime import datetime

from docopt import docopt

from sqlalchemy import Column, Integer, Sequence, String, Numeric, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

RAW_ATHLETTE_EVENTS    = 'history-athletes-and-results/athlete_events.csv'
PARSED_ATHLETTE_EVENTS = 'history-athletes-and-results/athlete_events_parsed.csv'
PARSED_CSV_FIELD_DELIM = '|'
VERSION = 'v20180819'

Base = declarative_base()

class Competitor(Base):
    __tablename__ = 'competitors'

    id          = Column(Integer, primary_key=True)
    name        = Column(String)
    sex         = Column(String)
    age         = Column(Integer)
    height      = Column(Numeric)
    weight      = Column(Numeric)
    team        = Column(String)
    noc         = Column(String)
    games       = Column(String)
    year        = Column(Integer)
    season      = Column(String)
    city        = Column(String)
    sport       = Column(String)
    event       = Column(String)
    metal       = Column(String)
    medal_value = Column(Integer)

    def __repr__(self):
        return '<Competitor id:{} name:{} s:{} a:{} games:{}>'.format(self.id, self.name, self.sex, self.age, self.games)


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=VERSION)
    print(arguments)

def parse_athlete_events():
    infile  = RAW_ATHLETTE_EVENTS
    outfile = PARSED_ATHLETTE_EVENTS
    print('parse_athlete_events: {}'.format(infile))
    fields  = "id|name|sex|age|height|weight|team|noc|games|year|season|city|sport|event|medal|medal_value".split('|')
    rows, row = list(), list()
    print("field count: {} {}".format(str(len(fields)), fields))
    
    # header row
    for field in fields:
        row.append(field)
    rows.append(row)

    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile)
        for idx, obj in enumerate(rdr):
            row = list()
            if idx < 300000:
                #print(obj)
                row.append(parse_int(obj['id']))
                row.append(parse_str(obj['name']))
                row.append(parse_str(obj['sex']).lower())
                row.append(parse_int(obj['age']))
                row.append(parse_float(obj['height']))
                row.append(parse_float(obj['weight']))
                row.append(parse_str(obj['team']).lower())
                row.append(parse_str(obj['noc']).lower())
                row.append(parse_str(obj['games']).lower())
                row.append(parse_int(obj['year']))
                row.append(parse_str(obj['season']).lower())
                row.append(parse_str(obj['city']).lower())
                row.append(parse_str(obj['sport']).lower())
                row.append(parse_str(obj['event']).lower())
                row.append(parse_str(obj['medal']).lower())
                row.append(medal_value(obj['medal']))
                rows.append(row)

    with open(outfile, 'w') as f:
        for row in rows:
            line = PARSED_CSV_FIELD_DELIM.join(row)
            #print(line)
            f.write(line)
            f.write("\n")
        print('file written: {}  count: {}'.format(outfile, len(rows)))

def query_azure_olympics_db():
    conn, cursor = None, None
    try:
        host    = os.environ['AZURE_PSQL_DB_SERVER']
        port    = os.environ['AZURE_PSQL_DB_PORT']
        user    = os.environ['AZURE_PSQL_DB_SERVER_ADMIN']
        dbname  = os.environ['AZURE_PSQL_DB_NAME']
        passwd  = os.environ['AZURE_PSQL_DB_PASS']
        sslmode = os.environ['AZURE_PSQL_DB_SSLMODE'] # disable, allow, prefer, require, verify-ca, verify-full

        # Construct connection string
        conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, passwd, sslmode)
        print("conn_string: {}".format(conn_string))

        conn = psycopg2.connect(conn_string) 
        print("Connection established")

        cursor = conn.cursor()
        print("Cursor obtained")

        sql = 'SELECT * FROM competitors limit 8;'
        print("executing sql: {}".format(sql))

        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            id   = row[0]
            name = row[1]
            print('{} {}'.format(str(id), name))
    except:
        print(sys.exc_info())
        traceback.print_exc()
    finally:
        if conn:
            conn.commit()
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def query_azure_olympics_db_orm():
    conn, cursor = None, None
    try:
        host    = os.environ['AZURE_PSQL_DB_SERVER']
        port    = os.environ['AZURE_PSQL_DB_PORT']
        user    = os.environ['AZURE_PSQL_DB_SERVER_ADMIN']
        dbname  = os.environ['AZURE_PSQL_DB_NAME']
        passwd  = os.environ['AZURE_PSQL_DB_PASS']
        sslmode = os.environ['AZURE_PSQL_DB_SSLMODE'] # disable, allow, prefer, require, verify-ca, verify-full

        conn_string = "postgresql+psycopg2://{}:{}@{}:{}/{}?sslmode=require".format(user, passwd, host, port, dbname)
        print("conn_string: {}".format(conn_string))
        engine = create_engine(conn_string)
        print('engine created')

        Session = sessionmaker(bind=engine)
        print('session class created')
        session = Session()
        print('session instance created')

        Base.metadata.create_all(engine)
        print('metadata created')

        # 34551|Allyson Michelle Felix
        afelix = session.query(Competitor).filter_by(id=34551).first() 
        print(afelix)

        # # Construct connection string
        # conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
        # print("conn_string: {}".format(conn_string))

        # conn = psycopg2.connect(conn_string) 
        # print("Connection established")

        # cursor = conn.cursor()
        # print("Cursor obtained")

        # sql = 'SELECT * FROM competitors limit 8;'
        # print("executing sql: {}".format(sql))

        # cursor.execute(sql)
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        #     id   = row[0]
        #     name = row[1]
        #     print('{} {}'.format(str(id), name))
    except:
        print(sys.exc_info())
        traceback.print_exc()
    finally:
        if conn:
            conn.commit()
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def parse_int(s):
    try:
        return str(int(s.strip()))
    except:
        return '-1'

def parse_float(s):
    try:
        return str(float(s.strip()))
    except:
        return '-1'

def parse_str(s):
    try:
        s1 = s.strip()
        if s1 == 'NA':
            s1 = ''
        s1 = s1.replace('"',"")
        s1 = s1.replace("'","")
        s1 = s1.replace(",","")
        s1 = s1.replace("|","")
        return s1
    except:
        return '?'

def medal_value(s):
    # gold, silver, bron
    try:
        s1 = s.strip().lower()
        if s1.startswith('g'):
            return '3'
        if s1.startswith('s'):
            return '2'
        if s1.startswith('b'):
            return '1'
        return '0'
    except:
        return '-1'


if __name__ == "__main__":

    start_time = time.time()

    if len(sys.argv) > 1:
        func = sys.argv[1].lower()

        if func == 'parse_athlete_events':
            parse_athlete_events()

        elif func == 'query_azure_olympics_db':
            query_azure_olympics_db()

        elif func == 'query_azure_olympics_db_orm':
            query_azure_olympics_db_orm()
        else:
            print_options('Error: invalid function: {}'.format(func))
    else:
        print_options('Error: no function argument provided.')
