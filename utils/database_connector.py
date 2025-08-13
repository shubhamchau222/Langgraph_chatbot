import sqlite3
from sqlite3 import Connection, Error
from typing import Optional
import logging
import os

# Configure module-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)


def getDBconnector(database_name: Optional[str] = None) -> Connection:
    """
    Create and return a thread-safe SQLite database connection.

    Args:
        database_name (Optional[str]): Path to the SQLite database file.
                                       Defaults to '../chatbot.db' relative to this file.

    Returns:
        sqlite3.Connection: SQLite connection object.

    Raises:
        sqlite3.Error: If connection cannot be established.
    """
    if database_name is None:
        # Default path relative to current file
        database_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../chatbot.db")

    try:
        conn = sqlite3.connect(
            database_name,
            check_same_thread=False  # Allows access from multiple threads
        )
        logger.info(f"Successfully connected to database: {database_name}")
        return conn
    except Error as e:
        logger.exception(f"Failed to connect to database {database_name}")
        raise e
    
# # Testing
# if __name__ == "__main__":
#     conn = getDBconnector()
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name TEXT)")
#     conn.commit()
#     conn.close()
    