import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "EmberitePass2234"
    )

mycursor = db.cursor()

mycursor.execute("NEW DATABASE emberiteDatabase")
