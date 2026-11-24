from flask import Blueprint, abort, jsonify, request

from app.db import get_connection

reports = Blueprint("reports", __name__)

SORTABLE_COLUMNS = {"created_at", "total", "status"}


@reports.get("/reports/orders")
def list_orders():
    column = request.args.get("sort", "created_at")
    if column not in SORTABLE_COLUMNS:
        abort(400)
    cursor = get_connection().cursor()
    cursor.execute("SELECT id, total, status FROM orders ORDER BY %s" % column)
    return jsonify(cursor.fetchall())
