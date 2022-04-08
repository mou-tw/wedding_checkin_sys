import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

tmp_info = {}

@app.route("/test_post/nn", methods = ['GET','POST'])
def test_post():
    tmp_info['name'] = 'test'
    tmp_info['age']  = '22'
    return json.dumps(tmp_info)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0',
            port = 8787,
            debug= True
    )