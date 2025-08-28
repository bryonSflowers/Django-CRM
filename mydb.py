#Install Mysql on computer
#pip intall.mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '903740C2FAfa.F800146716'

	)

#prepare a cursor object

cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE living4_database")

print ("All Done!")