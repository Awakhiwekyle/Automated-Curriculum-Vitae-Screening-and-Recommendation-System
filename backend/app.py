#!/usr/bin/ python
import datetime
import json
import math
from ast import literal_eval

from flask import (Flask, g, redirect,  request, session, jsonify, url_for)
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import func, desc, update, exists, asc
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
from views import *
from models import *
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
    # manager.run()
