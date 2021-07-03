from flask import Blueprint, jsonify

bp = Blueprint("probes", __name__, url_prefix="/probes")


@bp.route("/live")
@bp.route("/ready")
@bp.route("/startup")
def probe():
    return jsonify({})
