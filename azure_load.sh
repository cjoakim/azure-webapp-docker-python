#!/bin/bash

# Copy csv data into the Azure PostgreSQL olympics DB, competitors table
# Chris Joakim, Microsoft, 2018/08/19

echo 'loading db...'
echo $AZURE_PSQL_DB_PASS | pbcopy

psql --host=$AZURE_PSQL_DB_SERVER --port=$AZURE_PSQL_DB_PORT --username=$AZURE_PSQL_DB_SERVER_ADMIN --dbname=olympics -c "\copy competitors FROM '/Users/cjoakim/github/cj_data/olympics/history-athletes-and-results/athlete_events_parsed.csv' with (format csv, header true, delimiter '|');"

echo $USER | pbcopy

echo 'done'


# $ ./azure_load.sh
# loading db...
# Password for user cjoakim@cjoakimpsql:
# COPY 271116
# done
