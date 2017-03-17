#!/usr/bin/env python
# coding=utf-8

from flask_script import Command
import os

class Update(Command):

    print 'update envirement'

    def run(self):
        os.system('apt-get update')
