import re
import json
from flask import Flask, jsonify, render_template , request

app = Flask(__name__)

tmp_info = {}


def search_fuzzy_result(target ,s_lst):
    result = []
    pattern = '.*?'.join(target)
    regex = re.compile(pattern)
    for item in s_lst:
        match = regex.search(item)
        if match:
            result.append(item)
    return result



@app.route('/')
@app.route("/index")
def hello_world():
    return render_template("index2.html")

@app.route("/forword", methods=['GET', 'POST'])
def tmp():
    names = ['劉良玲','牟善群']
    print(request.values['name_search'])
    result = search_fuzzy_result(request.values['name_search'], names)
    print(result)
    return render_template("index2.html", names = result)


@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index2.html', forward_message=forward_message)



if __name__ == "__main__":
    app.run(host = '0.0.0.0',
            port = 8787,
            debug= True
    )