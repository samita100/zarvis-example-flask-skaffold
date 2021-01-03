from flask import Flask
import requests
import json
import os


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"



@app.route('/open')
def ope():
    os.system("while true; do python3 check.py && break; done & lscpu")


@app.route('/proxy')
def proxyi():
    response = requests.get('https://www.proxyscan.io/api/proxy?ping=100')
    jsons = json.loads(response.text)
    for i in jsons:
      ip = i["Ip"]
      port = i["Port"]
      t = i["Type"]
      tf = t[0].lower()
      final = f'{tf}://{ip}:{port}'
      print(final)
    return final






