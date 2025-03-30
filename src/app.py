from flask import Flask

from flask_restful import Api

from src.database import init_db

from src.apis.api import InvoxAPI


def create_app():

  app = Flask(__name__)
  app.config.from_object('src.config.Config')

  init_db(app)

  api = Api(app)
  api.add_resource(InvoxAPI, '/input_ai')

  return app


app = create_app()

