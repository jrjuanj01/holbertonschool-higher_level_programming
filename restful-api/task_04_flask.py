"""Developing a Simple API using Python with Flask"""
from flask import Flask, jsonify, request


app = Flask(__name__)


users = {}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return 'OK'


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.json()
    username = data.get('username')
    
    if not username: 
        return jsonify({'error': 'Username is required'}), 400    
    if username in users:
        return jsonify({'error': 'User already exists'}), 400
    users.update(data)

    return jsonify({
        'message': 'User added', 'user': data}), 201


@app.route("/user/<username>")
def profile(username):
    if username not in users:
        return jsonify({'error': 'User does not exist'}), 400
    else:
        return users[username]


if __name__ == '__main__':
    app.run(debug=True)
