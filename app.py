import json
import os
import platform
import sys

import arrow

from flask import Flask, render_template, request, send_file
from flask import Response

app = Flask(__name__, static_url_path='')

port = int(os.getenv("PORT"))

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
    return render_template('index.html')

@app.route('/list')
def images_list_route():
    return render_template('list.html')

@app.route('/noop')
def noop_route():
    filename = request.args.get('filename')
    if is_image_file(filename):
        print('noop: {}'.format(filename))
        return ('', 204)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)