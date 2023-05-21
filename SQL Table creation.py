import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='BrindhaGope',passwd="ReshuBindhu01*",database="programs")

mycursor = mydb.cursor() # point to particular location, connection with db, can execute,fetch,insert statement or db

mycursor.execute("select * from student")

result= mycursor.fetchall()

for i in result:
    print(i)
