import os
from contextlib import contextmanager
from psycopg2 import connect, extras

@contextmanager
def get_db_connection():
  """
  return db connection 
  """
  print("get_db_connection")
  try:
    conn = connect(user=os.getenv("DB_USER"), 
            host=os.getenv("DB_HOST"), 
            password=os.getenv("DB_PASS"), 
            port=os.getenv("DB_PORT"), 
            dbname=os.getenv("DB_NAME"))
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
  