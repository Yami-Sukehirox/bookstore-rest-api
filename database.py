import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="bookstore_db",
        cursorclass=pymysql.cursors.DictCursor  
    )