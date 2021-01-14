#!/usr/bin/python3

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        print("Connection established")
        # Create a new record
        # sql_1 = "INSERT INTO 'users' id MEDIUMINT NOT NULL AUTO_INCREMENT,"
        sql = "CREATE DATABASE `my_db;"
              #"(`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql)
        #('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(sql)
    connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT  `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #     result = cursor.fetchone()
    #     print(result)
except Exception as e:
    print(e)

finally:
    print("The connection has successfully been clsosed.")
    connection.close()












#
# # from __future__ import absolute_import
#
# import mysql.connector
#
#
# connection=mysql.connector(user="admi", password="password",host="localhost" )
#
# import unittest
#
# # Lunch@12:30!
#
# # CREATED BY :victor nkuna developerVNd
#
# password = input('enter mysql passwd:')
#
# connection_my=mysql.connector.connect(user="admi", password="password",host="localhost" )
#
# # /$ CREATE DATABASE lubuntu;
#
# #the  following command in  sql shell creates a database called lubuntu
#
#
#
#
#
#
#
#
#
# def create_connection(host_name,user_name,user_password):
#    try:
#        connection= mysql.connector.constants(
#            host=host_name,
#            user=user_name,
#            passwd=password)
#
#    except :
#        print("The error occurred '{}' occurred")
#    return connection
#
#
