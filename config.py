#!/usr/bin/env python
# coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True

#init superuser
SUPER_USER = "qdzzyb"
SECRET_KEY = "wlj199272"
#init database
USER_NAME = 'neal'
SQLALCHEMY_DATABASE_URI = f'postgresql://{USER_NAME}@localhost/blog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
