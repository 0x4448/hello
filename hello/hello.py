#!/usr/bin/env python3
import os
import platform
import random

from flask import Blueprint, abort, jsonify, request

bp = Blueprint("hello", __name__, url_prefix="/")


@bp.route("/")
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
