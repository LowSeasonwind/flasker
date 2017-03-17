#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from  app.asset import asset
from app.user import user


app = Flask(__name__)
app.register_blueprint(asset, url_prefix='/asset')
app.register_blueprint(user, url_prefix='/user')
