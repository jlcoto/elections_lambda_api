from http import HTTPStatus

from flask import Flask, jsonify

from db import DB, TABLE_NAME
from response_adapter import Adapter


adapter = Adapter()

app = Flask(__name__)

db = DB()


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hola {name}!"


@app.route("/get_all_results")
def get_all_results():
    results = db.client.scan(TableName=TABLE_NAME)
    return jsonify(adapter.adapt_party_data(results)), HTTPStatus.OK
