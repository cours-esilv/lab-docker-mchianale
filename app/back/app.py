import os
import sys
from flask import Flask
from flask_cors import CORS
from datetime import datetime

if 'CURRENT_ENVIRONMENT' not in os.environ:
    print('===================================================================', file=sys.stderr)
    print('[ERROR] Missing value for CURRENT_ENVIRONMENT envrionment variable.', file=sys.stderr)
    print('[ERROR] Please specify it when you start the container.', file=sys.stderr)
    sys.exit(1)

# Create logs folder
logs_dir = './logs'
if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)
elif not os.path.isdir(logs_dir):
    raise Exception(f"{logs_dir} exists and is not a directory")

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return {
        "time": str(datetime.now()),
        "environment": os.environ['CURRENT_ENVIRONMENT'],
        "hostname": os.uname()[1],
        "result": "root"
    }    

@app.route("/get/<name>")
def get(name):
    return {
        "time": str(datetime.now()),
        "environment": os.environ['CURRENT_ENVIRONMENT'],
        "hostname": os.uname()[1],
        "result": name
    }

@app.route("/write/<something>")
def write(something):
    print(something)
    with open('logs/my-messages.log', 'a') as the_file:
        the_file.write(f"{something}\n")
    return {
        "status": "ok"
    }