import os
import mysql.connector

HOST_DB = os.environ.get('HOST_DB')
USERNAME_DB = os.environ.get('USERNAME_DB')
PASSWORD_DB = os.environ.get('PASSWORD_DB')
DATABASE_DB = os.environ.get('DATABASE_DB')

mydb = mysql.connector.connect(
    host=HOST_DB,
    user=USERNAME_DB,
    password=PASSWORD_DB,
    database=DATABASE_DB
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
