import requests

from app import configuration


def check():
    containers_responses = []
    for port in range(configuration.config.START_PORT, configuration.config.END_PORT ):
        try:
            response = requests.get(f'http://{configuration.config.DOCKER_HOST}:{port}')
            containers_responses.append("Service at port:"+str(port)+" - Status code: " + str(response.status_code)+" - "+response.text)
        except:
            containers_responses.append(
                "Service at port:" + str(port) + " - Service unavailable")

    return containers_responses