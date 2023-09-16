import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "EmberitePass2234",
    database = "emberiteDatabase"
    )

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("DESCRIBE Person")
#mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Tim", 19))
#db.commit()

'''
mycursor.execute("INSERT INTO userTable (userId, firstName, lastName, age, gender, ethnicity, occupation, adminFlag, activeFlag)\
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (1, "Connor", "Paladino", 20, 'M', "Caucasian", "Student", 0, 1))

                 
                 
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses)\
                 VALUES (%s,%s,%s)", (1, "9/16/2023", 184723))

mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses)\
                 VALUES (%s,%s,%s)", (1, "9/16/2023", 938275))

mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses)\
                 VALUES (%s,%s,%s)", (1, "9/16/2023", 123857))

mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses)\
                 VALUES (%s,%s,%s)", (1, "9/16/2023", 957392))


mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses)\
                 VALUES (%s,%s,%s)", (1, "9/17/2023", 938275))

mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses)\
                 VALUES (%s,%s,%s)", (1, "9/18/2023", 123857))

mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses)\
                 VALUES (%s,%s,%s)", (1, "9/19/2023", 957392))



mycursor.execute("INSERT INTO loginTable (userID, username, password)\
                 VALUES (%s,%s,%s)", (1, "testConnor", "testPassword"))



mycursor.execute("INSERT INTO userTable (userId, firstName, lastName, age, gender, ethnicity, occupation, adminFlag, activeFlag)\
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (2, "Admin", "Test", 22, 'M', "Caucasian", "Student", 1, 1))

mycursor.execute("INSERT INTO loginTable (userID, username, password)\
                 VALUES (%s,%s,%s)", (2, "testAdmin", "testAdminPassword"))

'''

mycursor.execute("SELECT *  FROM questionTable")

for x in mycursor:
    print(x)

#db.commit()