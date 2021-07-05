#!/usr/bin/env python3
import os
import platform
import random

from flask import Blueprint, abort, jsonify, request

bp = Blueprint("hello", __name__, url_prefix="/")

# View counter for index
index_counter = 0


@bp.route("/")
def index():
    # Return 500 occasionally if environment variable ERROR_RATE is defined.
    try:
        if float(os.environ.get("ERROR_RATE", 0)) > random.random() * 100:
            abort(500, description="randomly generated error")
    except ValueError:
        # Ignore invalid values for ERROR_RATE.
        pass

    # Increment view counter
    global index_counter
    index_counter += 1

    # Return 500 if counter exceeds environment variable LIMIT.
    try:
        if index_counter > int(os.environ.get("LIMIT", "")):
            abort(500, description="limit exceeded")
    except ValueError:
        # Ignore invalid values for LIMIT
        pass

    response = {
        "client_ip": request.remote_addr,
        "hostname": platform.node(),
        "counter": index_counter,
    }
    return jsonify(response)


@bp.route("/env")
def env():
    return jsonify(dict(os.environ))
