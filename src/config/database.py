import mysql.connector
import pymysql

mydb = mysql.connector.connect(
    host="localhost",
    user="user_stey",
    password="123456",
    database="stey_db"
)


class DatabaseConnection:

    def __init__(self):
        self.client = mydb

    def get(self, sql):
        cursor = self.client.cursor(dictionary=True)

        cursor.execute(sql)

        result = cursor.fetchall()
        cursor.close()
        return result

    def insert(self, sql, values):
        cursor = self.client.cursor(dictionary=True)

        cursor.execute(sql)

        self.client.commit()
        cursor.close()
