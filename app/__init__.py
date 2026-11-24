from flask import Flask

from app.routes.auth import auth
from app.routes.imports import imports
from app.routes.pages import pages
from app.routes.proxy import proxy
from app.routes.reports import reports
from app.routes.tools import tools
from app.routes.users import users


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "flask-session-signing-key-do-not-share-2024"
    for blueprint in (auth, imports, pages, proxy, reports, tools, users):
        app.register_blueprint(blueprint)
    return app
