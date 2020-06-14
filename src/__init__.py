from flask import Flask

from src.config import load_config
from src.blueprint import (
  blueprint,
  hello,
)

def create_app():
  """An application factory."""
  load_config()
  app = Flask(__name__)

  app.config.from_object(__name__)

  app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
  app.debug = True

  # register blue print
  register_blueprints(app)

  return app


def register_blueprints(app):
  """Register Flask blueprints."""
  app.register_blueprint(blueprint)
  app.register_blueprint(hello.blueprint)