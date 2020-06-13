import json
from flask import Blueprint, Response, request, jsonify

blueprint = Blueprint('root', __name__)

@blueprint.route("/")
def root():
  return jsonify("safe!")