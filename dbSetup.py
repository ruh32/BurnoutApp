import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "EmberitePass2234",
    database = "emberiteDatabase"
    )

mycursor = db.cursor()


#userTable data mapping
'''
mycursor.execute("CREATE TABLE userTable (userID INT PRIMARY KEY,\
                 firstName VARCHAR(50),\
                 lastName VARCHAR(50),\
                 age SMALLINT UNSIGNED,\
                 gender CHAR(1),\
                 ethnicity VARCHAR(50),\
                 occupation VARCHAR(50),\
                 adminFlag BIT,\
                 activeFlag BIT)")
'''

mycursor.execute("CREATE TABLE questionTable (userID INT PRIMARY KEY,\
                 date VARCHAR(50),\
                 questionResponses INT)")


db.commit()

