#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import os
import csv
import database
import sqlite3

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
    parameter_id = request.args.get('id')
    list_products = []
    url_json = 'products.json'
    url_csv = 'products.csv'
    db = database
    if query_parameter == 'json' and parameter_id is None:
        if os.path.exists(url_json):
            try:
                with open(url_json, "r") as archivo:
                    data = json.load(archivo)
                    list_products = data
            except json.JSONDecodeError:
                print('archivo invalido')
            return render_template('product_display.html', products=list_products)

    elif query_parameter == 'csv' and parameter_id is None:
        if os.path.exists(url_csv):
            try:
                with open(url_csv, newline='') as csvfile:
                    data = csv.DictReader(csvfile, delimiter=',')
                    for fila in data:
                        list_products.append(fila)
            except csv.Error:
                print('archivo invalido')
            return render_template('product_display.html', products=list_products)

    elif query_parameter == 'sql' and parameter_id is None:
        conn = None
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            for row in rows:
                list_products.append(dict(row))
            return render_template('product_display.html', products=list_products)
        except sqlite3.Error:
            print('archivo invalido')
            return render_template('product_display.html', mensaje="problemas de coneccion")
        finally:
            if conn:
                conn.close()
    elif parameter_id:
        parameter_id = int(parameter_id)
        with open(url_json, "r") as archivo:
                    data = json.load(archivo)
                    for prod in data:
                        if prod['id'] == parameter_id:
                            list_products.append(prod)
        if len(list_products) != 0:
            return render_template('product_display.html', products=list_products)
        else:
            return render_template('product_display.html', mensaje="Product not found")
    else:
        return render_template('product_display.html', mensaje="Wrong source")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
