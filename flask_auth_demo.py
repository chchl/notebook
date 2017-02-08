#!/usr/bin/env python
#-*-coding:UTF-8-*-

from flask import Flask, url_for, render_template, request, flash, \
    redirect, make_response, jsonify, g
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.comfig['SECRET_KEY'] = 'secret key'

auth = HTTPBasicAuth()

books = ['The Name of the Rose', 'The Historian', 'Rebecca']
users = [
    {'username':'ethan', 'password':generate_password_hash('6666')},
    {'username':'peter', 'password':generate_password_hash('9527')},
]

@auth.verify_password
def verify_password(username, password):
    user = filter(lambda user: user['username'] == username, users)
    if user and check_password_hash(user[0]['password'], password):
        g.user = username
        return True
    return False

@app.route('/', methods=['GET'])
def index():
    return render_template(
        'book.html',
        books=books
    )

@app.route('/', methods=['POST'])
def add_book():
    _form = request.form
    title = _form["title"]
    if not title:
        return '<h1>invalid request</h1>'

    books.append(title)
    flask("add book successfully!")
    return redirect(url_for('index'))

@auth.error_handler
def unauthrized():
    return make_response(jsonify(
        {'error': 'Unauthorized access'}
    ), 401)

if __name__ == '__main__':
    app.run(debug=True)

