# coding : utf-8
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
  redis.incr('hits')
  return 'Hello Docker Book reader! I have been seen {0} times'

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

