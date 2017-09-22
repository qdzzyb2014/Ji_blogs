#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_alembic import Alembic
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
alembic = Alembic()
alembic.init_app(app)
Markdown(app)

from app import views, models
