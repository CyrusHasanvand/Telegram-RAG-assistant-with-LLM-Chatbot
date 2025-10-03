import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",       
            password="XXXXXX",  
            database="ChatBotDB2"
        )
        print('Cyrus: Connected to the DB')
        return conn
    except Error as e:
        print(f"Cyrus: Database connection error: {e}")
        return None

def save_chat(user_id, username, message, reply):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        sql = """INSERT INTO logs (user_id, username, message, reply) 
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (user_id, username, message, reply))
        conn.commit()
        cursor.close()
        conn.close()
        print('Cyrus: New saving process in MySQL')


print('Cyrus: Everything is OK')
