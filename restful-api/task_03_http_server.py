#!/usr/bin/python3
"""
esta modulo configura un server con python, hasta el momento el
codigo envia un mensaje con codigo 200 y el mensaje 
hello, this is a simple api
"""


import http.server
import socketserver
import requests

PORT = 8000

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
