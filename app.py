from flask import Flask, request, jsonify, send_file
import os 
import json

dirname = os.path.dirname(__file__)
home = os.path.join(dirname, 'static', 'index.html')

app = Flask(__name__)





@app.route('/', methods=["GET"])

def index():
    return send_file(home)


@app.route("/api/<state>",methods=["POST"])
def powerState(state):
    print(state)
    return state


if __name__ == "__main__":
    app.run()
    