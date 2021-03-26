from http import HTTPStatus

import boto3
from flask import Flask, jsonify

from response_adapter import Adapter

session = boto3.Session(profile_name="jose_default")

adapter = Adapter()

app = Flask(__name__)

TABLE_NAME = "electionResults"

db_client = session.client("dynamodb", region_name="eu-central-1")


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hola {name}!"


@app.route("/get_all_results")
def get_all_results():
    results = db_client.scan(TableName=TABLE_NAME)
    return jsonify(adapter.adapt_party_data(results)), HTTPStatus.OK
