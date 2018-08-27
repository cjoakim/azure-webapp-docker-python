drop table competitors;

-- "ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"
-- "1","A Dijiang","M",24,180,80,"China","CHN","1992 Summer",1992,"Summer","Barcelona","Basketball","Basketball Men's Basketball",NA

-- psql template1
-- alter user postgres with password 'password';
-- alter user cjoakim  with password 'password';
-- create database olympics owner cjoakim;

-- psql -d olympics -f /Users/cjoakim/github/cj_data/olympics/history-athletes-and-results/olympics-psql.sql
-- DROP TABLE
-- CREATE TABLE
--
-- $ psql olympics
-- olympics=# \d 
-- olympics=# \d competitors
-- olympics=# select count(*) from competitors;  --> 271116
-- olympics=# select * from competitors where metal like '%G%';
-- olympics=# select * from competitors where age < 20 limit 4;

CREATE TABLE competitors (
    id          integer not null,
    name        character varying(200) not null,
    sex         character(1) null,
    age         integer not null,
    height      numeric not null,
    weight      numeric not null,
    team        character varying(100) null,
    noc         character varying(6) null,
    games       character varying(100) null,
    year        integer null,
    season      character varying(10) null,
    city        character varying(40) null,
    sport       character varying(100) null,
    event       character varying(100) null,
    metal       character varying(6) null,
    medal_value integer not null
);

COPY competitors(id, name, sex, age, height, weight, team, noc, games, year, season, city, sport, event, metal, medal_value) 
FROM '/Users/cjoakim/github/cj_data/olympics/history-athletes-and-results/athlete_events_parsed.csv' DELIMITER '|' CSV HEADER;
