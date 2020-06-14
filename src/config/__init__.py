import os
from dotenv import load_dotenv
from pathlib import Path 

def load_config():
  """Load Config from .env at root project"""
  env_path = Path('.') / '.env'
  load_dotenv(dotenv_path=env_path, verbose=True)

def config():
  """get all config values"""
  return {
    "APP_ENV": os.getenv("APP_ENV"),
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_PORT": os.getenv("DB_PORT"),
    "DB_NAME": os.getenv("DB_NAME"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASS": os.getenv("DB_PASS"),
  }