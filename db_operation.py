import pymysql.cursors

# Connect to the database
# try:
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='hospitals',
                             charset='utf8mb4')



cursor=connection.cursor()



sql =  "SELECT * FROM Login"

sql_10 = "INSERT INTO Login  VALUES('Skylar','Sky2021');"
sql_11 = "INSERT INTO Login  VALUES('Lwando','Lwa2021');"
sql_12 = "INSERT INTO Login  VALUES('Zenanade','Zen2021');"

cursor.execute(sql)
cursor.execute(sql_10)
cursor.execute(sql_11)
cursor.execute(sql_12)



results = cursor.fetchall()  #this will return a list of each rowin a table called "Patients"
for  row in results:
    print(row)

connection.commit()
connection.close()
