import sqlite3

def createTable():
    connection = sqlite3.connect('login.db')
    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,PASSWORD TEXT,DEVICE TEXT,MAC TEXT)")

    connection.execute("INSERT INTO USERS VALUES(?,?,?,?)",('Kssj4','KRI','16','16'))

    connection.commit()

    result = connection.execute("SELECT * FROM USERS")

    for data in result:
        print("Username : ",data[0])
        print("PASSWORD : ",data[1])
        print("DEVICE",data[2])
        print("MAC :",data[3])

    connection.close()

createTable()
