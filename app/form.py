#!/usr/bin/env python
# coding=utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import DataRequired


class LoginForm(Form):
    user_name = StringField('user_name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('登陆')


class EditForm(Form):
    title = StringField('title', validators=[DataRequired()])
    content = TextAreaField('entry', validators=[DataRequired()])
