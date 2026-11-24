import os

from flask import Blueprint, render_template_string, request, send_file

from app.config import UPLOAD_DIR

pages = Blueprint("pages", __name__)


@pages.get("/hello")
def hello():
    name = request.args.get("name", "guest")
    return render_template_string(f"<h1>Hello {name}</h1>")


@pages.get("/files")
def download():
    filename = request.args["name"]
    return send_file(os.path.join(UPLOAD_DIR, filename))
