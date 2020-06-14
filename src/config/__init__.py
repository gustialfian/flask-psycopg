import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only

class Config:
  __instance = None
  
  @staticmethod 
  def get_instance():
    """ Static access method. """
    if Config.__instance == None:
      Config()
    return Config.__instance
  
  def __init__(self):
    """ Virtually private constructor. """
    if Config.__instance != None:
      raise Exception("This class is a singleton!")
    Config.__instance = self
    
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path, verbose=True)

    self.values = {
      "APP_ENV": os.getenv("APP_ENV"),
      "DB_HOST": os.getenv("DB_HOST"),
      "DB_PORT": os.getenv("DB_PORT"),
      "DB_NAME": os.getenv("DB_NAME"),
      "DB_USER": os.getenv("DB_USER"),
      "DB_PASS": os.getenv("DB_PASS"),
    }
    
    print("load config file")
    print(self.values)
