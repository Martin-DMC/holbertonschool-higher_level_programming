#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import os
import csv

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

@app.route('/products')
def products():
    query_parameter = request.args.get('source')
    list_products = []
    url_json = 'products.json'
    url_csv = 'products.csv'
    if query_parameter == 'json':
        if os.path.exists(url_json):
            try:
                with open(url_json, "r") as archivo:
                    data = json.load(archivo)
                    list_products = data
            except json.JSONDecodeError:
                print('archivo invalido')
            return render_template('product_display.html', products=list_products)
    elif query_parameter == 'csv':
        if os.path.exists(url_csv):
            try:
                with open(url_csv, newline='') as csvfile:
                    data = csv.DictReader(csvfile, delimiter=',')
                    list_products = data
            except:
                pass
            return render_template('product_display.html', products=list_products)
    else:
        return render_template('product_display.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
