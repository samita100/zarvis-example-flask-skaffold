from flask import Flask
import threading
import requests
import json
import time
import os


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"



@app.route('/open')
def ope():
    threading.Thread(target=hop).run()
    return "Done"

def hop():
    while true:
      os.system("python3 check.py")
      time.sleep(5)

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






