import user
import entry
import questionnaire
import resources
import loginCheck

#test user check
currUser = user.User(1)
print(currUser.id)
print(currUser.get_firstname())
print(currUser.get_lastname())
print(currUser.get_age())
print(currUser.get_gender())
print(currUser.get_ethnicity())
print(currUser.get_occupation())
print(currUser.get_admin_status())
print(currUser.get_active_status())

#check questionnaire class
userQs = questionnaire.Questionnaire(1)
entryDict = userQs.getDict()
print(entryDict)

#check login checker class
checker = loginCheck.LoginCheck()
check = checker.checkValid("testConnor", "testPassword1")
print(check)
check = checker.checkValid("testConnor", "testPassword")
print(check)
getId = checker.getUserID("testConnor", "testPassword")
print(getId)