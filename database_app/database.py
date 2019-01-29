# Import connection pool tools from psycopg2
from psycopg2 import pool


# Create a class to create a connection to the database
class Database:
    # Create connection_pool property in class
    __connection_pool = None

    @staticmethod
    # Initialize connection with keyword arguments passed in, set pool range between 1 and 12 connections
    def init_conn(**kwargs):
        Database.__connection_pool = pool.SimpleConnectionPool(1, 12, **kwargs)
        # kwargs(keyword args) = named parameters in app.py

    # Method: To get a connection from pool
    @staticmethod
    def get_connection():
        return Database.__connection_pool.getconn()

    # Method: Returns the connection to the pool when finished
    @staticmethod
    def return_connection(connection):
        Database.__connection_pool.putconn(connection)

    # Method: Closes open connections
    @staticmethod
    def close_all_connections():
        Database.__connection_pool.closeall()


# Create a class to open a cursor to manipulate the database. Use with statement(init, enter, exit)
class ConnectionPool:
    def __init__(self):
        # Create connection property
        self.connection = None
        # Create cursor property
        self.cursor = None

    def __enter__(self):
        # Return a valid new connection from the pool
        self.connection = Database.get_connection()
        # Get cursor from connection
        self.cursor = self.connection.cursor()
        # return active connection with cursor
        return self.cursor

    # Close cursor Commit data and return connection to the pool
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Rollback connection if error occurs
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()  # Close cursor
            self.connection.commit()  # Commit data
        # Return connection to the pool
        Database.return_connection(self.connection)
