import sqlite3

connection  = sqlite3.connect("login1.db")
c = connection.cursor()
username = "firoj"
password = "asd"
result = c.execute("Select * From USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
rows = result.fetchall()
if(len(rows) > 0):
	for row in rows:
		print(row)
		print(row[0], row[1], row[3])
