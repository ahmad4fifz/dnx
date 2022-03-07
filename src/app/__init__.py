"""API blueprint configuration."""
from flask import Blueprint, Flask
from flask_restx import Api

from app.route.domain import domain_ns

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    api_bp,
    version="1.0",
    title="API for dnx using Flask-RESTX",
    description="Welcome to the Swagger UI documentation site!",
    doc="/docs",
)

api.add_namespace(domain_ns, path="/domain")


def create_app():
    app = Flask("__name__")
    app.register_blueprint(api_bp)
    return app
