#!/usr/bin/python3
"""Developing a Simple API using Python with Flask"""
from flask import Flask, jsonify


app = Flask(__name__)


users = {"jane": {"username": "jane", "name": "Jane",
                  "age": 28, "city": "Ponce"},
         "tito": {"username": "tito", "name": "Tito",
                  "age": 40, "city": "Aguadilla"},
         "pedro": {"username": "pedro", "name": "Pedro",
                   "age": 30, "city": "Ponce"},
         "error": "user not found"}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    return jsonify(users)


@app.route("/status")
def status():
    return 'OK'


@app.route("/user/<username>")
def profile(username):
    if username not in users:
        return users["error"]
    else:
        return users[username], 404


if __name__ == '__main__':
    app.run(debug=True)
