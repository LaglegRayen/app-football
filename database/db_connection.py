import pymysql


def create_connection():
    """Create a database connection to the MySQL database."""
    connection = None
    try:
        connection = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        if connection in locals():
            print("Connection to the database was successful.")
    except pymysql.Error as e:
        print(f"The error '{e}' occurred")
    return connection

def close_connection(connection):
    """Close the database connection."""
    if connection and connection in locals():
        connection.close()
        print("The connection to the database has been closed.")