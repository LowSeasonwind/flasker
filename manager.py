#!/usr/bin/env python
# coding=utf-8

from flask_script import Manager
from app import app
import config

app.config.from_object(config)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
