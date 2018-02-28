#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Simple proxy server in python using Flask

"""
__description__ = 'Python HTTP Proxy Server with Flask'
__author__ = 'Maikel D. F.'
__author_email__ = 'maikeldf@gmail.com'
__license__ = 'BSD'

import requests
import flask
from flask import Flask, Response

app = flask.Flask(__name__)

target_server = 'http://localhost:5000/'

@app.route("/", methods=['GET', 'POST'])
def streamed_proxy():
    print ("http method: ",flask.request.method)
    
    if flask.request.method == 'POST':
      r = requests.post(target_server, stream=True)
    else: 
      if flask.request.method == 'GET':
         r = requests.get(target_server, stream=True)
      
    print ("HEADERS", r.headers)
    return Response(r.iter_content(chunk_size=10*1024),
                    content_type=r.headers['Content-Type'])

if __name__ == "__main__":
    app.run(port=1234)