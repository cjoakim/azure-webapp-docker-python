#!/bin/bash

# Open a psql client to the Azure PostgreSQL olympics DB
# Chris Joakim, Microsoft, 2018/08/19

echo $AZURE_PSQL_DB_PASS | pbcopy

psql --host=$AZURE_PSQL_DB_SERVER --port=$AZURE_PSQL_DB_PORT --username=$AZURE_PSQL_DB_SERVER_ADMIN --dbname=olympics

echo $USER | pbcopy


# $ ./azure_psql.sh
# Password for user cjoakim@cjoakimpsql:
# psql (10.5, server 9.6.9)
# SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-SHA384, bits: 256, compression: off)
# Type "help" for help.

# olympics=> \d
#                    List of relations
#  Schema |        Name        | Type  |      Owner
# --------+--------------------+-------+-----------------
#  public | competitors        | table | cjoakim
#  public | pg_buffercache     | view  | azure_superuser
#  public | pg_stat_statements | view  | azure_superuser
# (3 rows)

# olympics=> select count(*) from competitors;
#  count
# --------
#  271116
# (1 row)

# olympics=> \d competitors;
#                       Table "public.competitors"
#    Column    |          Type          | Collation | Nullable | Default
# -------------+------------------------+-----------+----------+---------
#  id          | integer                |           | not null |
#  name        | character varying(200) |           | not null |
#  sex         | character(1)           |           |          |
#  age         | integer                |           | not null |
#  height      | numeric                |           | not null |
#  weight      | numeric                |           | not null |
#  team        | character varying(100) |           |          |
#  noc         | character varying(6)   |           |          |
#  games       | character varying(100) |           |          |
#  year        | integer                |           |          |
#  season      | character varying(10)  |           |          |
#  city        | character varying(40)  |           |          |
#  sport       | character varying(100) |           |          |
#  event       | character varying(100) |           |          |
#  metal       | character varying(6)   |           |          |
#  medal_value | integer                |           | not null |

# olympics=>
