import os, requests
from flask import Flask

app = Flask(__name__)

try: import env
except ImportError:
    # no env module but heroku may have set env var
    try: os.environ['YO_KEY']
    except KeyError:
        print 'Dawg, you need to set your YO_KEY!'

@app.route('/yo')
def yo():
    token = { "api_token": os.environ['YO_KEY'] }
    yoall = "http://api.justyo.co/yoall/"
    requests.post(yoall, data=token)
    return 'Yo!'
