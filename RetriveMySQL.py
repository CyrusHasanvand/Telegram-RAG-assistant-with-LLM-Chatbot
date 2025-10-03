import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",       
            password="kalmakare",  
            database="ChatBotDB2"
        )
        print('Cyrus: Connected to the DB')
        return conn
    except Error as e:
        print(f"Cyrus: Database connection error: {e}")
        return None

def fetch_chats(limit=50):
    conn = connect_db()
    if conn:
        cursor = conn.cursor(dictionary=True)  # dictionary=True → results as dict
        sql = "SELECT user_id, username, message, reply, create_at FROM logs ORDER BY create_at DESC LIMIT %s"
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        print('Cyrus: The data was retrieved as rows')
        return rows
    return []


print('Cyrus: Everything is OK')
