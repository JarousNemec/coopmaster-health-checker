import requests

from app import configuration


def check():
    containers_responses = []
    for port in range(configuration.start_port, configuration.end_port):
        response = requests.get(f'http://{configuration.docker_host}:{port}')
        containers_responses.append("Service at port:"+str(port)+" - Status code: " + str(response.status_code)+" - "+response.text)
    return containers_responses