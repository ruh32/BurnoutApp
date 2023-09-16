class User:
    def __init__(self, id, username, password, firstName, lastName, age, gender, ethnicity, occupation, adminFlag, active):
        self.id = id
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.ethnicity = ethnicity
        self.occupation = occupation
        self.adminFlag = adminFlag
        self.active = active
    
    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
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

