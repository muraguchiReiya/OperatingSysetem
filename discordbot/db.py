# -*- coding: utf-8 -*-
import pandas as pd
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
#con=conect_db()
#query="CREATE DATABASE IR"
#create_database(con,query)
#create_IR_table = "CREATE TABLE IR (id INT,name VARCHAR(40),year INT,month INT,day INT,time VARCHAR(10),start_time VARCHAR(10),end_time VARCHAR(10),content VARCHAR(80));"
#con=create_db_connection() # データベースに接続
#delete_table="DROP TABLE IR"
#con=execute_query(con,delete_table)
#con=execute_query(con, create_IR_table)
#insert_data="INSERT INTO IR VALUES(023,'test2',2022,12,22,'03:00','12:00','15:00','作業');"
#con=execute_query(con,insert_data)
#query="SELECT * FROM IR;"
#results=read_query(con,query)
#for result in results:
    #print(result)
#send_query(insert_data)
#query(insert_data)
#queryOfread(query)
