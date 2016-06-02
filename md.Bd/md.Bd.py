# based on https://gist.github.com/kemitche/9749639

from flask import Flask
app = Flask(__name__)

import requests
import json
import urllib

# how to obscure keys in github?
# dealing with oauth is a pain!! see if there is a better library?
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "https://127.0.0.1:5000/pin_call"

# runs on localhost
# url app: http://127.0.0.1:5000
# redirect app: https://127.0.0.1:5000/pin_call

# do you need to store users in a database?
@app.route("/pin_call")

def hello():
	return "Hiiii"



#Oauth redirect

# test endpoint from Pinterest
r = requests.get("")
r.text
data.json.loads(r.text)


if __name__ == "__main__":
	app.run()



