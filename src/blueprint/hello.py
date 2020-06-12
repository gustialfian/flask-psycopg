import json
from flask import Blueprint, Response, request, jsonify

from src.database import get_db_cursor

blueprint = Blueprint('hello', __name__,)

@blueprint.route("/")
def hello():
  return jsonify("hello world")


@blueprint.route("/db")
def db():
  with get_db_cursor() as cursor:
    cursor.execute("select now()")
    data = cursor.fetchone()
    return jsonify(data)