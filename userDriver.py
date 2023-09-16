import user
import entry
import questionnaire
import resources

#test user check
currUser = user.User(1)
print(currUser.userID)
print(currUser.get_firstname())
print(currUser.get_lastname())
print(currUser.get_age())
print(currUser.get_gender())
print(currUser.get_ethnicity())
print(currUser.get_occupation())
print(currUser.get_admin_status())
print(currUser.get_active_status())