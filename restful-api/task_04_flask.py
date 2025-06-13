#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>¡Welcome to the Flask API!</h1>'

@app.route('/data')
def data():
    users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
    }
    dato = jsonify(users)
    return dato

if __name__ == "__main__":
    app.run(debug=True)