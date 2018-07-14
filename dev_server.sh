#!/bin/bash

# Bash script to start the Flask web app in development mode
# with auto restarts upon code changes.
# Chris Joakim, 2018/07/14

export FLASK_APP=app.py

python -m flask run --debugger --port 3000
