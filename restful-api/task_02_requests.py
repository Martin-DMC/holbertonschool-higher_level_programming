#!/usr/bin/python3
"""
"""
import requests
import csv


def fetch_and_print_posts():
    """"""
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status code: {respuesta.status_code}")
    if respuesta.status_code == 200:
        py_dicts = respuesta.json()
        for dic in py_dicts:
            print(dic["title"])

def fetch_and_save_posts():
    """"""
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta == 200:
        return csv.DictWriter(respuesta, 'posts.csv')
