#!/bin/bash

# Bash script to start Flask on port 3000 in development mode
# with auto restarts upon code changes.
# Chris Joakim, 2018/07/09

export FLASK_APP=app.py

python -m flask run --debugger --port 3000
