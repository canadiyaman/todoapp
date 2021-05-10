import os
from environs import Env

env = Env()
# Read .env into os.environ
path = os.getcwd()
env.read_env(".env")


SECRET_KEY = env('SECRET_KEY', 'FAKE_PASSWORD')
DATABASE_URL = env('DATABASE_URL', 'sqlite:///db.sqlite3')
DEBUG = env.bool('DEBUG', False)
