from flask import Flask,make_response,jsonify
import json

app = Flask(__name__)


@app.route('/index',methods=["GET"])
def index():
    data = {
        "name":"liguang",
        "age":"15"
    }
    json_str = json.dumps(data)
    return json_str,200,{"Content-Type":"application/json"}


if __name__ == '__main__':
    app.run(debug=True)
