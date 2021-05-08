from flask import Flask
from generators import *
app = Flask('app')

@app.route('/')
def homepage():
  return "Todo: Finish Homepage"

app.run(host='0.0.0.0', port=8080)