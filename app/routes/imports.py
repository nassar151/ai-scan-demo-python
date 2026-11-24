import pickle

import yaml
from flask import Blueprint, jsonify, request

imports = Blueprint("imports", __name__)


@imports.post("/imports/cart")
def import_cart():
    cart = pickle.loads(request.data)
    return jsonify({"items": len(cart)})


@imports.post("/imports/settings")
def import_settings():
    settings = yaml.load(request.data, Loader=yaml.Loader)
    return jsonify(settings)
