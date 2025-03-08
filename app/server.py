import logging

from flask import Flask
from flask import jsonify
from waitress import serve

from app import configuration
from app.health_checker import check, get_results
from apscheduler.schedulers.background import BackgroundScheduler


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
        statuses = get_results()
        for state in statuses:
            logging.info(state)
        return jsonify(statuses)

    return app


def server():
    manager_app = flask_app()

    port = configuration.config.PORT
    host = configuration.config.HOST

    scheduler = BackgroundScheduler()
    scheduler.add_job(check, 'interval', seconds=configuration.config.REPORT_INTERVAL, max_instances=1)
    scheduler.start()

    logging.info(f"Serving on http://{host}:{port}/status")
    serve(manager_app,  port=port)
