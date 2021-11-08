from os import getenv
from pathlib import Path

from environs import Env


def get_config():
    config = dict()
    env = Env()
    env.read_env()  # read .env file if it exists

    PORT = getenv('PORT', 8080)
    HOST = getenv('HOST', '0.0.0.0')
    config['HOST'] = HOST
    config['PORT'] = PORT
    return config
