import urllib.request
import requests
import json



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

  x1 = requests.post(url1, data=json.dumps(myobj1), headers=headers1)
  print(x1.text)
