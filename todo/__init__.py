from flask import Flask
from flask_graphql import GraphQLView

from todo.api.schema import schema


def create_app(settings_override=None):
    app = Flask(__name__)
    if settings_override:
        app.config.update(settings_override)

    routes(app)
    return app


def routes(app):

    @app.route("/")
    def hello():
        return "Go to /graphql"

    view_func = GraphQLView.as_view("graphql",
                                    schema=schema,
                                    middleware=[],
                                    graphiql=True)

    app.add_url_rule('/graphql', view_func=view_func)
