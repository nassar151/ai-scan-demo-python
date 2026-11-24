import requests
from flask import Blueprint, jsonify, request

proxy = Blueprint("proxy", __name__)


@proxy.get("/proxy/preview")
def preview():
    url = request.args["url"]
    response = requests.get(url, verify=False, timeout=5)
    return jsonify({"status": response.status_code, "length": len(response.content)})
