#!/usr/bin/python3

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/items')
def items():
    list_items = []
    if os.path.exists('items.json'):
        try:
            with open('items.json', "r") as archivo:
                data = json.load(archivo)
            if (data):
                list_items = data['items']
        except json.JSONDecodeError:
            print('archivo invalido')
        except KeyError:
            print(f'el archivo no contiene la clave esperada')
    return render_template('items.html', items=list_items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
