#!/usr/bin/env python
# coding=utf-8


from flask import render_template
from app.asset import asset



@asset.route('/')
def index():
    return render_template('asset/index.html',title='Asset',where='Asset')
