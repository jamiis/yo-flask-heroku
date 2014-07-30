import os, requests
from flask import Flask
from tokens import YO_TOKEN

app = Flask(__name__)

@app.route('/yo')
def yo():
    token = { "api_token": YO_TOKEN }
    yo_all = "http://api.justyo.co/yoall/"
    r = requests.post(yo_all, data=token)
    return 'Yo!'
