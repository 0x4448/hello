from flask import Flask, jsonify

from . import hello, probes


def internal_server_error(e):
    return jsonify(error=str(e)), 500


def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello.bp)
    app.register_blueprint(probes.bp)

    app.register_error_handler(500, internal_server_error)

    return app


app = create_app()
