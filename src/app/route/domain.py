from app.core.engine import dnx
from app.model.domain import domain_model, domain_reqparser
from flask_restx import Namespace, Resource
import validators

domain_ns = Namespace(name="domain", validate=True)
domain_ns.models[domain_model.name] = domain_model


@domain_ns.route("/query", endpoint="domain_query")
class DomainQuery(Resource):
    """Handles HTTP requests to URL: /api/v1/domain/query."""

    @domain_ns.expect(domain_reqparser)
    def get(self):
        """Query single domain and return result in JSON."""
        request_data = domain_reqparser.parse_args()
        domain = request_data.get("domain")
        if validators.domain(domain):
            return dnx(domain)
        else:
            return {"message": "Invalid domain name"}, 400


@domain_ns.route("/querydb", endpoint="domain_querydb")
class DomainQuery(Resource):
    """Handles HTTP requests to URL: /api/v1/domain/querydb."""

    @domain_ns.expect(domain_reqparser)
    def get(self):
        """Query single domain from database. If no record in database, engine will query and and return result in JSON and save in database."""
        request_data = domain_reqparser.parse_args()
        domain = request_data.get("domain")
        if validators.domain(domain):
            dnx(domain)
            
        else:
            return {"message": "Invalid domain name"}, 400
