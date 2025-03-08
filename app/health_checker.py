import json
import logging

import requests

from app import configuration

results = []


def check():
    global results
    results = []
    services = configuration.get_services_locations()

    for service in services:
        try:
            parts = service.split(':')
            response = requests.get(f'http://{service}', timeout=5)
            report = f"Service at port: {parts[1]} - Status code: {response.status_code} - {response.text}"
            logging.info(report)
            results.append(report)
        except:
            results.append(f"Service at {parts[0]}:{parts[1]} - Service unavailable")


def get_results():
    global results
    return results
