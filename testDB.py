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

mycursor.execute("INSERT INTO userTable (userId, firstName, lastName, age, gender, ethnicity, occupation, adminFlag, activeFlag)\
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (1, "Connor", "Paladino", 20, 'M', "Caucasian", "Student", 0, 1))

        

mycursor.execute("INSERT INTO loginTable (userID, username, password)\
                 VALUES (%s,%s,%s)", (1, "testConnor", "testPassword"))



mycursor.execute("INSERT INTO userTable (userId, firstName, lastName, age, gender, ethnicity, occupation, adminFlag, activeFlag)\
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (2, "Admin", "Test", 22, 'M', "Caucasian", "Student", 1, 1))

mycursor.execute("INSERT INTO loginTable (userID, username, password)\
                 VALUES (%s,%s,%s)", (2, "testAdmin", "testAdminPassword"))



mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-07-14',221858)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-07-21',854735)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-06-17',962783)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-06-14',463144)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-08-07',441241)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-08-31',178274)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-09-05',885863)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-09-08',898936)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-07-28',864984)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-07-23',669383)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-08-13',586283)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-07-11',413765)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-06-30',994917)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-06-15',222314)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-07-23',169765)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-08-23',156589)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-06-16',619556)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-09-07',725221)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (1,'2023-07-15',199982)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-09-13',576559)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-08-29',517488)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-08-08',434542)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-07-01',568282)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-08-18',882623)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-06-23',418835)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-07-23',296789)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-08-13',913164)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-07-16',172323)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-09-11',539759)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-08-09',551475)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-06-14',749561)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-07-10',459476)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-06-19',714782)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-08-06',737577)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-07-20',385776)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-08-27',944167)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-08-14',757885)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-06-27',136657)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-07-25',884221)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (2,'2023-06-21',581753)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-07-22',524388)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-06-30',166339)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-07-03',661688)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-07-27',182317)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-07-11',295735)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-06-17',278823)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-06-14',592964)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-08-18',393345)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-09-10',144157)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-09-14',629193)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-09-05',761213)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-07-12',695575)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-07-15',785916)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-06-09',286948)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (3,'2023-06-11',375988)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-07-08',215233)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-09-09',897124)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-08-16',765674)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-09-06',663325)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-07-05',657587)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-09-07',213417)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-08-07',648784)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-08-20',355633)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-08-01',439726)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-07-17',278143)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-09-02',652842)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-07-25',316115)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-07-13',216932)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (4,'2023-06-16',277743)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-06-09',159286)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-08-17',515745)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-07-28',663753)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-07-21',292497)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-07-10',611284)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-07-12',282799)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-07-04',329211)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-07-16',426575)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-07-29',946467)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-08-14',355643)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-09-12',558352)")
mycursor.execute("INSERT INTO questionTable (userId, date, questionResponses) VALUES (5,'2023-08-11',266734)")
                 
db.commit()
