"""Parsers and serializers for /domain API endpoints."""
from flask_restx import Model
from flask_restx.fields import String
from flask_restx.reqparse import RequestParser


domain_reqparser = RequestParser(bundle_errors=True)
domain_reqparser.add_argument(
    name="domain", type=str, location="args", required=True, nullable=False
)

domain_model = Model(
    "Domain",
    {
        "email": String,
        "fuzzer": String,
        "domain": String,
        "dns_a": String,
        "dns_aaaa": String,
        "dns_mx": String,
        "dns_ns": String,
        "geoip": String,
    },
)
