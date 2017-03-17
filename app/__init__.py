#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from  app.asset import asset


app = Flask(__name__)
app.register_blueprint(asset, url_prefix='/asset')
