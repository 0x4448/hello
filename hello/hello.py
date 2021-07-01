#!/usr/bin/env python3
import os
import platform
import random

from flask import Flask, abort, jsonify, request

app = Flask(__name__)


# Error handlers
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500


# Views
@app.route("/")
def index():
    # Return 500 occasionally if environment variable ERROR_RATE is defined.
    try:
        if float(os.environ.get("ERROR_RATE", 0)) > random.random() * 100:
            abort(500, description="randomly generated error")
    except ValueError:
        # Ignore invalid values for ERROR_RATE.
        pass

    response = {
        "client_ip": request.remote_addr,
        "hostname": platform.node(),
    }
    return jsonify(response)


@app.route("/ready")
@app.route("/startup")
def startup():
    return jsonify({})
