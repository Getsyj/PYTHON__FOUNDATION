import mysql.connector
from util.db_property_util import read_db_config

def get_connection():
    config = read_db_config()
    connection = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    return connection


if __name__ == "__main__":
    try:
        conn = get_connection()
        if conn.is_connected():
            print("✅ Successfully connected to the database.")
            conn.close()
        else:
            print("❌ Failed to connect.")
    except Exception as e:
        print("❌ Error:", e)
