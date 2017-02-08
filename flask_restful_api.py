#! /usr/bin/env python
#-*-coding:UTF-8-*-

from flask import Flask
from flask_restful import Resource,reqparse,Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Hello':'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
