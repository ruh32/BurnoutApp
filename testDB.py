import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "EmberitePass2234",
    database = "testdatabase"
    )

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("DESCRIBE Person")
#mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Tim", 19))
#db.commit()

mycursor.execute("SELECT max(personID) FROM Person")

for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)
