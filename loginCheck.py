import mysql.connector

class LoginCheck:

    def __init__(self):
        self

    def checkValid(self, username, password) -> bool:

        db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "EmberitePass2234",
        database = "emberiteDatabase"
        )

        mycursor = db.cursor()

        mycursor.execute("SELECT count(*) FROM loginTable WHERE username LIKE %s AND password LIKE %s", (username, password))
        
        for x in mycursor:
            if x[0] == 0:
                return False
        
        return True
    

    def getUserID(self, username, password) -> int:

        db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "EmberitePass2234",
        database = "emberiteDatabase"
        )

        out, holdU, holdP = -1, '', ''

        mycursor = db.cursor()

        mycursor.execute("SELECT * FROM loginTable WHERE username LIKE %s AND password LIKE %s", (username, password))

        for userID, username, password in mycursor:
            out = userID
            holdU = username
            holdP = password
        
        return out
