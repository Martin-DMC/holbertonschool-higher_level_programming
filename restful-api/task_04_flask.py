#!/usr/bin/python3
"""
this module is for develop a Simply API using Python with Flask
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """
    this function return a simple message of welcome"""
    return '¡Welcome to the Flask API!', 200


@app.route('/status')
def estado():
    """
    this function return only of status"""
    return 'OK', 200


@app.route('/data')
def data():
    """
    this function return all usernames stored in the global variable 'users'
    """
    lista = list(users.keys())
    return jsonify(lista), 200


@app.route('/user/<username>')
def user_name(username):
    """
    this function return a full data of the specified user in the route
    Returns:
        successful the data specified or a error for not found"""
    try:
        return jsonify(users[username]), 200
    except KeyError:
        return jsonify({'error': 'User not found'}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    this function be used for add users in the 'data base'
    returns:
        a message for sussesful action and error for a exception
        of missing data"""
    data_user = request.get_json()
    try:
        key = data_user['username']
    except KeyError:
        return {"error": "Username is required"}, 400
    users[key] = data_user
    retorno = {'message': 'user added', 'user': data_user}
    return jsonify(retorno), 201


if __name__ == "__main__":
    app.run(debug=True)
