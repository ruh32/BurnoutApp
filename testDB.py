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
'''

#db.commit()

mycursor.execute("SELECT * FROM userTable WHERE userID = 1")
for x1, x2, x3, x4, x5, x6, x7, x8, x9 in mycursor:
    print(x1)
    print(x2)
    print(x3)
    print(x4)
    print(x5)
    print(x6)
    print(x7)
    print(x8)
    print(x9)

