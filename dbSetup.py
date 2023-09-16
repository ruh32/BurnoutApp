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

#questionTable data mapping
'''
mycursor.execute("CREATE TABLE questionTable (userID INT PRIMARY KEY,\
                 date VARCHAR(50),\
                 questionResponses INT)")
'''

#journal data mapping
'''
mycursor.execute("CREATE TABLE journalTable (userID INT PRIMARY KEY,\
                 date VARCHAR(50),\
                 journalEntry TEXT)")
'''

#resource mappings
'''
mycursor.execute("CREATE TABLE resourceTable (name VARCHAR(50) PRIMARY KEY,\
                 url TINYTEXT,\
                 phone INT UNSIGNED,\
                 logo VARCHAR(50),\
                 description TEXT,\
                 activeFlag BIT)")

mycursor.execute("CREATE TABLE loginTable (userID INT PRIMARY KEY,\
                 username VARCHAR(50),\
                 password VARCHAR(50))")

                 '''

#db.commit()

