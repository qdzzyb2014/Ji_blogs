#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('config')
#app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)
lm = LoginManager()
lm.setup_app(app)
Markdown(app)

from app import views, models
