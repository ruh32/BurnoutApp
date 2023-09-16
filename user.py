class User:
    def __init__(user, id, username, password, firstName, lastName, age, gender, ethnicity, occupation, adminFlag, active):
        user.id = id
        user.username = username
        user.password = password
        user.firstName = firstName
        user.lastName = lastName
        user.age = age
        user.gender = gender
        user.ethnicity = ethnicity
        user.occupation = occupation
        user.adminFlag = adminFlag
        user.active = active
    
    def get_id(user):
        return user.id
    
    def get_username(user):
        return user.username
    
    def get_lastname(user):
        return user.lastName
    
    def get_age(user):
        return user.age
    
    def get_gender(user):
        return user.gender
    
    def get_ethnicity(user):
        return user.ethnicity
    
    def get_occupation(user):
        return user.occupation
    
    def get_admin_status(user):
        return user.adminFlag
    
    def get_active_status(user):
        return user.active

