#!/usr/bin/env python
# coding=utf-8

from flask_wtf import FlaskForm as Form
from wtforms import TextField
from wtforms.validators import DataRequired

class MyForm(Form):
    name = TextField('name', validators = [DataRequired()])
