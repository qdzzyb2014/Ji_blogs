#!/usr/bin/env python
# coding=utf-8
from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    pub_date = db.Column(db.DateTime, index = True)

    def __repr__(self):
        return '<Entry titile: %r>' % (self.title)

