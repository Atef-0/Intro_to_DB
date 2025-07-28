import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
    )
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(e)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed.")
    