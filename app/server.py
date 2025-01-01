import logging

from flask import Flask
from flask import jsonify
from waitress import serve

from app import configuration
from app.health_checker import check


def flask_app():
    app = Flask('__main__')

    @app.route("/")
    def hello_world():
        message = "Hello World  from health checker"
        logging.info(message)
        return message

    @app.route("/status")
    def status():
        logging.info("Containers status:")
        statuses = check()
        for state in statuses:
            logging.info(state)
        return jsonify(statuses)

    return app


def server():
    manager_app = flask_app()

    port = configuration.config.PORT
    host = configuration.config.HOST

    logging.info(f"Serving on http://{host}:{port}/status")
    serve(manager_app,  port=port)
