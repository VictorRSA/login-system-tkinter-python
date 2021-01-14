
import pymysql.cursors

# Connect to the database
# try:
#localhost = "127.0.0.1 " is the ip address of the mysql database server

connection = pymysql.connect(host='localhost',
                             #I can use host ="127.0.0.1"
                             user='root',
                             password='',
                             database='hospitals',
                             charset='utf8mb4'

                             )



cursor=connection.cursor()

#     # Create a new record
# # sl_0 ="CREATE TABLE STATION (ID INTEGER PRIMARY KEY,CITY CHAR(20),STATE CHAR(2),LAT_N REAL,LONG_W REAL);"
# # cursor.execute(sl_0)
# sql = "INSERT INTO Dentists VALUES ('BNF450002', 'Boniface', 'Dr.Simons', 0772563698, 10005267888);"
# sql2="INSERT INTO Dentists VALUES ('MS56000012','Sarah-Maggies','Dr.Moosa',0115062089,1254888052);"
# sql3 ="INSERT INTO Dentists VALUES ('RAY800203', 'Raymond', 'Dr.Okereke', 0137228936, 1042455028);"
# sql4 = "INSERT INTO Dentists VALUES('TM5892009','Tebogo','Dr.Mphahlele',0122220781,1254052077);"
#
# sql_1 = "INSERT INTO Patients  VALUES(10025,'Kelebohile','Khosi','Medical Aid','Gems','MS5600012');"
# sql_2 = "INSERT INTO Patients  VALUES(10026,'Tamara','Said','Cash','None','MS5600012');"
# sql_3 = "INSERT INTO Patients  VALUES(10027,'Nonso','Diobi','Medical Aid','Bonitas','TM5892009');"
# sql_4 = "INSERT INTO Patients  VALUES(10028,'Fiona','Lampard','Medical Aid','Trinite','RAY800203');"
# sql_5 = "INSERT INTO Patients  VALUES(10029,'Salmina','Troy','Cash','None','BNF450002');"
# sql_6 = "INSERT INTO Patients  VALUES(10030,'Willy','Thompson','Cash','None',' BNF450002');"
# sql_7 = "INSERT INTO Patients  VALUES(10031,'Kingsley','Slyvic','Medical Aid','Bonitas','TM5892009');"
# sql_8 = "INSERT INTO Patients  VALUES(10032,'Millicent','Michael','Medical Aid','Gems','TM5892009');"
# sql_9 = "INSERT INTO Patients  VALUES(10033,'Majid','Michel','Medical Aid','Trinite',' MS5600012');"
# sql_10 = "INSERT INTO Patients  VALUES(10034,'Ada','Collins','Medical Aid','Gems','RAY800203');"





#
# cursor.execute()
# cursor.execute(sql_2)
# cursor.execute(sql_3)
# cursor.execute(sql_4)
# cursor.execute(sql_5)
# cursor.execute(sql_6)
# cursor.execute(sql_7)
# cursor.execute(sql_8)
# cursor.execute(sql_9)
# cursor.execute(sql_10)
#
# Nkuna NKuna
sql =  "SELECT * FROM Dentists"
# sql2 = "UPDATE Dentists SET Dentist_surname =Nkuna WHERE Dentist_surname=Roberts"
# cursor.execute(sql2)
# sql3 = "INSERT INTO Dentists VALUES ('NKNVIC003','Victor','NKuna',0760170851,1234567890);"
# sql3_1 = "UPDATE Dentists SET Dentist_names ='Victor Robert' WHERE Dentist_surname ='NKuna';"
# cursor.execute("SHOW DATABASES")
# sql = cursor.execute(sql)

for item in cursor:
    print(item)

connection.commit()


# finally:
    # close the database connection using close() method.
connection.close()
