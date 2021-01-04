from flask import Flask
import requests
import json
import os
import threading

def tar():
    os.system("watch -n 7 python3 check.py")


threading.Thread(target=tar).run()


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World :)"






