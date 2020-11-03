from flask import Flask, request, jsonify, send_file
import os 
app = Flask(__name__)





@app.route('/', methods=["GET"])

def index():
    return send_file("index.html")
    