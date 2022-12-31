# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
class DB:
    def __init__(self,db_name,user_password,user_name,host_name):
        self.db_name=db_name
        self.user_password=user_password
        self.user_name=user_name
        self.host_name=host_name

    def read_query(self,connection,query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            return err
    def create_database(self,connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")
    def create_db_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        return connection
    def execute_query(self,connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
            #return connection
            return "データベースに登録されました"
        except Error as err:
            print(f"Error: '{err}'")
            return err
    def read_query(self,connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            return err
