import requests

from app import configuration


def check():
    containers_responses = []
    docker_host = configuration.config.DOCKER_HOST

    for port in range(configuration.config.START_PORT, configuration.config.END_PORT):
        try:
            response = requests.get(f'http://{docker_host}:{port}')
            containers_responses.append(
                f"Service at port: {port} - Status code: {response.status_code} - {response.text}")
        except:
            containers_responses.append(f"Service at {docker_host}:{port} - Service unavailable")

    return containers_responses
