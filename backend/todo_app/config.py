import os
from environs import Env

env = Env()
# Read .env into os.environ
path = os.getcwd()
env.read_env(".env")


SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', False)
