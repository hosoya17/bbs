from flask import Flask
app = Flask(__name__)

import os
app.secret_key = os.urandom(24)

import flaskr.main

from flaskr import db
db.create_bbs_table()
