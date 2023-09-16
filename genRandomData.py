import mysql.connector
import random, datetime

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=100)
random_date = start_date + (end_date - start_date) * random.random()
print(random_date.date())

def printRandom(id):


    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "EmberitePass2234",
        database = "emberiteDatabase"
        )

    mycursor = db.cursor()

    for i in range(30):
        randomResponse = int(999999 * random.random())
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=100)
        random_date = start_date + (end_date - start_date) * random.random()
        print("mycursor.execute(\"INSERT INTO questionTable (userId, date, questionResponses) VALUES (" + str(id) + "," + str(random_date.date()) + "," + str(randomResponse) + ")\")")
        
printRandom(1)
printRandom(2)
printRandom(3)
printRandom(4)
printRandom(5)