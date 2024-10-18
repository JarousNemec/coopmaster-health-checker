import logging
import requests

from flask import Flask, json, jsonify
from waitress import serve

from app import configuration
from app.health_checker import check


def flask_app():
    app = Flask('__main__')

    @app.route("/")
    def hello_world():
        logging.info("Hello World!")
        return configuration.hello_message

    @app.route("/status")
    def status():
        logging.info("Containers status:")
        statuses = check()
        for status in statuses:
            logging.info(status)
        return jsonify(statuses)

    return app

def server(host: str = "127.0.0.1", port: int = 80, ssl: bool = False):
    manager_app = flask_app()

    logging.info("Serving on http://"+configuration.host+":"+str(port))
    serve(manager_app,  port=port)