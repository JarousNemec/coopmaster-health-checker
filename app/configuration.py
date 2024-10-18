import os

host = "127.0.0.1"
port = 9000
hello_message = "Hello from health checker!"

log_file_name = "health_checker.log"

def get_log_directory():
    return "./logs/"

def get_log_filename():
    return log_file_name