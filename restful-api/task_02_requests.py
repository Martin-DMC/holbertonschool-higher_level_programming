#!/usr/bin/python3
"""
this module is a basic python script to fetch posts from
JSONPlaceholder using request.get()
"""
import requests
import csv


def fetch_and_print_posts():
    """
    This function gets the posts from jsonplaceholder and
    if the status code is ok (200) it prints all the post titles.
    """
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {respuesta.status_code}")
    if respuesta.status_code == 200:
        py_dicts = respuesta.json()
        for dic in py_dicts:
            print(dic["title"])


def fetch_and_save_posts():
    """
    this function get the posts and if status code is ok (200)
     make/open a file and save all post in format of file.csv
    """
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        py_dicts = respuesta.json()
        lista_csv = []
        for dic in py_dicts:
            _id = dic['id']
            title = dic['title']
            body = dic['body']
            new_dic = {'id': _id, 'title': title, 'body': body}
            lista_csv.append(new_dic)
        filas = lista_csv[0].keys()
        with open("posts.csv", mode="w", newline='') as archivo:
            constructor = csv.DictWriter(archivo, fieldnames=filas)
            constructor.writeheader()
            constructor.writerows(lista_csv)
