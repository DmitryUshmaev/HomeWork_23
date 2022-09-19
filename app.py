import os

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from builder import build_query
from models import RequestParams, BatchRequestParams

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query() -> jsonify:
    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as e:
        return e.messages, 400

    result = None

    for query in params['queries']:
        result = build_query(cmd=query['cmd'], param=query['value'], data=result)

    return jsonify(result)


app.run()
