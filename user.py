import mysql.connector


class User:
    def __init__(self, id):

        db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "EmberitePass2234",
        database = "emberiteDatabase"
        )

        mycursor = db.cursor()

        mycursor.execute("SELECT * FROM userTable WHERE userID = %s" % id)
        
        for userId, first, last, age, gender, ethnicity, occupation, admin, active in mycursor:
            self.id = userId
            self.firstName = first
            self.lastName = last
            self.age = age
            self.gender = gender
            self.ethnicity = ethnicity
            self.occupation = occupation
            self.adminFlag = admin
            self.active = active

        print("Successfully Called User")
    
    @classmethod

    def get_id(self):
        return self.id
    
    def get_firstname(self):
        return self.firstName
    
    def get_lastname(self):
        return self.lastName
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def get_ethnicity(self):
        return self.ethnicity
    
    def get_occupation(self):
        return self.occupation
    
    def get_admin_status(self):
        return self.adminFlag
    
    def get_active_status(self):
        return self.active

