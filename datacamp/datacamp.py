#Created by:Victor Nkuna
#Created on: 17 December 2020


import pymysql.cursors

# Connect to the database
# try:
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='my_db',
                             charset='utf8mb4')

cursor = connection.cursor()

#lets us check the connection objetc first

# print("The number of databases present in our MYSQL DB server is:",cursor.execute("SHOW DATABASES"))
# print()
# database = cursor.fetchall()
# """fetchall() method fetches all the rows from the last executed statement"""
# databases = cursor.fetchall() #it returns a ;ist of all databases present in the MYSQL DATABASE SERVER""""
# print("The list of all the databases in our db server are")
# print(databases)
#
#
# print()
#
# print("Showing the databases list one by one")
#
# print()
#
# for db in databases:
#     print(db)
#
#
#
# #
# """sql = "CREATE TABLE users (name VARCHAR(255),user_name VARCHAR(255));" """
# cursor.execute("SHOW TABLES;")
#
#
# tables = cursor.fetchall()
# #it returns list of tables present in my_db databases
#
# #showing all the tables  one by None
#
#
# for table in tables:
#     print("The following table(s) exist in our database called:'my_db'")
#     print(table)
#
#

# cursor.execute("DROP TABLE users;")
sql = "CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255) NOT NULL,user_name VARCHAR(255) NOT NULL);"
# cursor.execute(sql)
sql2 = "DESCRIBE users;"

# print(cursor.execute(sql2))
sql3 = "DROP TABLE users;"
# cursor.execute(sql2)

# print(cursor.fetchall())

# print(cursor.fetchall())

sql4 = "ALTER TABLE users DROP id;"  #we are dropping a primary key from already inserted data

# cursor.execute(sql4)

"""Adding Primary Key to the existing table ,we use ALTER TABLE table_name ADD PRIMARY KEY (column_name) statement to add a Primary key to table"""
sql4 = "ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST"


# cursor.execute(sql4)
cursor.execute("DESCRIBE users")

# print(cursor.fetchall())


"""INserting data into table to store it,Use INSERT INTO table_name  column_name VLAUES(data)statment to insert into a table"""

"""inserting into a single row or entry,or sample"""


sql5= "INSERT INTO users (name,user_name) VALUES(%s ,%s)"

## storign values in a variables

values = ("Victor","Nkuna")


##executing the quejry with the values in

# cursor.execute(sql5,values)
connection.commit()

print(cursor.rowcount,"Record inserted")

