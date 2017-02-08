#!/usr/bin/env python
#-*-coding:UTF-8-*-

from flask_script import Command
from flask_script import Manager
from flask import Flask

app = Flask(__name__)
manager = Manager(app)
#class Hello(Command):
#
#    def run(self):
#        print 'Hello world'
#
#manager.add_command('hello', Hello())
#
@manager.option('-n','--name',help='Your name')
def hello(name):
    print 'hello', name

if __name__ == '__main__':
    manager.run()
