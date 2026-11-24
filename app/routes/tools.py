import subprocess

from flask import Blueprint, jsonify, request

tools = Blueprint("tools", __name__)


@tools.post("/tools/ping")
def ping():
    host = request.json["host"]
    output = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True)
    return jsonify({"output": output.stdout})
