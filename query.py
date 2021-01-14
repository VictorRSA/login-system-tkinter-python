import pymysql.cursors
import datetime
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='hospitals',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

cur = connection.cursor()
now =  datetime.datetime.now()
# cur.execute("USE hospitals;")

# print(cur.execute("SAVEPOINT;"))
# sql_n = "INSERT INTO Patients VALUES (102050,'Godwin','Dr.Dzvapatsva','Cash','None','RAY800203');"
# sql2 = "SELECT * FROM Patients;"
sql2 = "SAVEPOINT 15_Dec_2020;"
sql3 = "ROLLBACK TO 15_Dec_2020;"
sql4 = "DELETE FROM Patients WHERE Paitent_Names='Godwin';"
sql_0 = "COMMIT;"
# cur.execute(sql4)
desc = "DESCRIBE Patients;"
# print(cur.execute(desc))


sql =  "SELECT * FROM Patients"
cur.execute(sql)

# results = cur.fetchall()  #this will return a list of each rowin a table called "Patients"
# for  row in results:
#     print(row)
# # cur.execute()

connection.commit()

connection.close()
