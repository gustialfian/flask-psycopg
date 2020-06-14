from contextlib import contextmanager
from psycopg2 import connect, extras

from src.config import Config

@contextmanager
def get_db_connection():
  """
  return db connection 
  """
  print("get_db_connection")
  config = Config.get_instance().values
  try:
    conn = connect(user=config.DB_USER, 
            host=config.DB_HOST, 
            password=config.DB_PASS, 
            port=config.DB_PORT, 
            dbname=config.DB_NAME)
    # ini apa ???
    # conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    yield conn
  finally:
    conn.close()


@contextmanager
def get_db_cursor():
  """
  psycopg2 connection.cursor context manager.
  Creates a new cursor and closes it, commiting changes if specified.
  """
  print("get_db_cursor")
  with get_db_connection() as connection:
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    try:
      yield cursor
    finally:
      cursor.close()


class DB:
  