from flask import Flask
import requests
import json
import urllib.request


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"



@app.route('/open')
def ope():
    try:
      urllib.request.urlopen("https://onlineedlreg.dotm.gov.np/dlNewRegHome").getcode()
      #urllib.request.urlopen("https://google.com").getcode()
  
      url = 'https://hooks.slack.com/services/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'
      myobj = {"text":"UP :)"}
      headers = {'content-type': 'application/json'}

      x = requests.post(url, data=json.dumps(myobj), headers=headers)

      print(x.text)
  
  
    except:
      print("Unable to open the website")
      url1 = 'https://hooks.slack.com/services/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'
      myobj1 = {"text":"DOWN :("}
      headers1 = {'content-type': 'application/json'}

      x = requests.post(url1, data=json.dumps(myobj1), headers=headers1)
    return "Done"





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






