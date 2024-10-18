import os

host = "127.0.0.1"
docker_host = "host.docker.internal"
port = 9000
hello_message = "Hello from health checker!"
start_port = 9001
end_port = 9009
log_file_name = "health_checker.log"

def get_log_directory():
    return "./logs/"

def get_log_filename():
    return log_file_name