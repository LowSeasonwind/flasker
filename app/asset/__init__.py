#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint

asset = Blueprint('asset', __name__)

import views
