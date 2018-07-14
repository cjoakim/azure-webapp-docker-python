#!/bin/bash

# Recreate the virtual environment and reinstall libs.
# Requires Python 3
# Chris Joakim, 2018/07/14

rm -rf tmp/
rm txt_merged.txt
rm pip-selfcheck.json
rm pyvenv.cfg

docker build -t cjoakim/webapp-docker-python . 

docker image ls | grep webapp-docker-python

echo 'done'
