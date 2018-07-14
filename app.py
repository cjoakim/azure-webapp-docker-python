import datetime
import json
import os
import platform
import sys
import time

import arrow

from flask import Flask, render_template, request, send_file
from flask import Response

print('__name__: {}'.format(__name__))
app = Flask(__name__, static_url_path='')

port = int(os.getenv("PORT", default=80))
print('port: {}'.format(port))

def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

@app.before_first_request
def before_first_request():
    try:
        print('before_first_request')
    except Exception as e:
        app.logger.error(str(e))

@app.before_request
def before_request():
    try:
        pass
    except Exception as e:
        app.logger.error(str(e))

@app.route('/')
def index_route():
    data = dict()
    data['date'] = datetime.datetime.now()
    data['time'] = time.time()
    return render_template('index.html', data=data)

@app.route('/env')
def images_list_route():
    env_vars = list()
    for env_var_name in sorted(os.environ):
        env_var = dict()
        env_var['name'] = env_var_name
        env_var['value'] = os.getenv(env_var_name)
        env_vars.append(env_var)
    return render_template('env.html', env_vars=env_vars)

# private

def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

def write_lines(lines, outfile):
    with open(outfile, "w", newline="\n") as out:
        for line in lines:
            out.write(line)
            out.write("\n")
        print('file written: {}'.format(outfile))


print('run port: {}'.format(port))
app.run(host=None, port=port)
