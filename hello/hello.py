#!/usr/bin/env python3
import platform

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    response = {
        "client_ip": request.remote_addr,
        "hostname": platform.node(),
    }
    return jsonify(response)


@app.route("/ready")
@app.route("/startup")
def startup():
    return jsonify({})
