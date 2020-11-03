from flask import Flask, request, jsonify, send_file
import os 

dirname = os.path.dirname(__file__)
home = os.path.join(dirname, 'static', 'index.html')

app = Flask(__name__)





@app.route('/', methods=["GET"])

def index():
    # return send_file("index.html")
    return send_file(home)

if __name__ == "__main__":
    app.run()
    