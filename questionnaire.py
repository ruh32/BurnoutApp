import mysql.connector

class Questionnaire:
    
    def __init__(self, id):

        db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "EmberitePass2234",
        database = "emberiteDatabase"
        )

        mycursor = db.cursor()

        mycursor.execute("SELECT * FROM questionTable WHERE userID = %s" % id)

        self.user_id = id
        self.responseDict = dict()

        for userId, date, response in mycursor:
            self.responseDict[date] = response
        



    
    @classmethod
    def get_id(self):
        return self.user_id
    
    def get_question_response(self, i):
        return self.responseDict.getValue(i)
    
    def set_question_response(self, date, answer):
        self.responseDict.append(date, answer)

    def getDict(self):
        return self.responseDict.copy()
