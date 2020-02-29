import sqlite3

connection  = sqlite3.connect("login1.db")
c = connection.cursor()
result = c.execute("create table USERS(USERNAME VARCHAR(20), PASSWORD VARCHAR(20), DEVICE VARCHAR(20), MAC VARCHAR(20), FILE VARCHAR(1000))")
connection.commit()
#result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ? AND MAC = ?",(username,password,mac))
#if(len(result.fetchall()) > 0):
	