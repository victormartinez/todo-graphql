from flask import Flask
from flask_graphql import GraphQLView

from todo import settings
from todo.api.schema import schema
from todo.extensions import db


def create_app(settings_override=None):
    app = Flask(__name__)

    config(app, settings_override)
    routes(app)
    extensions(app)
    return app


def config(app, settings_override):
    app.config["DEBUG"] = settings.DEBUG

    if settings_override:
        app.config.update(settings_override)


def routes(app):
    @app.route("/")
    def hello():
        return "Go to /graphql"

    view_func = GraphQLView.as_view("graphql",
                                    schema=schema,
                                    middleware=[],
                                    graphiql=True)

    app.add_url_rule('/graphql', view_func=view_func)


def extensions(app):
    db.init_app(app)