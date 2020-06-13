import json
from flask import Blueprint, Response, request, jsonify

from src.database import get_db_cursor

blueprint = Blueprint('hello', __name__, url_prefix='/hello')


@blueprint.route("/db")
def db():
  with get_db_cursor() as cursor:
    cursor.execute("select now()")
    data = cursor.fetchone()
    return jsonify(data)

  
@blueprint.route("/query")
def query():
  if request.args:
    # We have our query string nicely serialized as a Python dictionary
    args = request.args
    # We'll create a string to display the parameters & values
    serialized = ", ".join(f"{k}: {v}" for k, v in request.args.items())
    # Display the query string to the client in a different format
    return f"(Query) {serialized}", 200

  return "No query string received", 200

@blueprint.route("/methods", methods=["GET","POST"])
@blueprint.route("/methods/<id>", methods=["PUT", "DELETE"])
def methods(id=None):
  if request.method == "POST":
    return post_methods()

  if request.method == "PUT":
    return put_methods(id)

  if request.method == "DELETE":
    return delete_methods(id)

  return get_methods()


def get_methods():
  print(request.args)
  return jsonify("hit get")

def post_methods():
  print(request.get_json())
  return jsonify("hit post")

def put_methods(id):
  print(request.get_json())
  print(id)
  return jsonify("hit put")

def delete_methods(id):
  print(id)
  return jsonify("hit delete")
