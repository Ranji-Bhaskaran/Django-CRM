# pip install mysql
# pip install mysql-connector-python
# pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd = 'Gova@2003'

)
 

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE Gushy")

print("All Done!!")



