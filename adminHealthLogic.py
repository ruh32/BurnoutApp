import user, healthLogic, questionnaire, cgi, datetime, statistics, plotly.express as px, mysql.connector
import os
import matplotlib.pyplot as plt
import seaborn as sns

def getTeamAverage():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "EmberitePass2234",
        database = "emberiteDatabase"
        )

    mycursor = db.cursor()
    mycursor.execute("SELECT userID from userTable")

    teamAverage = []
    i = 0

    for x in mycursor:
        id = x
        temp = healthLogic.HealthLogic(id)
        teamAverage[i] = temp.getHealthMonthAverage()
        i+=1

    return sum(teamAverage) / len(teamAverage)

def makeTeamGraph():
        
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "EmberitePass2234",
    database = "emberiteDatabase"
    )

    mycursor = db.cursor()
    mycursor.execute("SELECT userID from userTable")


    newDict = dict()

    for x in mycursor:
        id = x
        getResponses = questionnaire.Questionnaire(id)
        tempDict = getResponses.getDict()
        newDict.update(tempDict)
    
    sorted_dict = dict(reversed(sorted(newDict.items())))
    for key in sorted_dict:
        sorted_dict[key] /= 100000

    plt.figure()
    plt.title("Overall Company Health Score")
    sns.lineplot(x=list(sorted_dict.keys()), y=list(sorted_dict.values())).invert_yaxis()
    plt.xlabel("Date")
    plt.xticks(range(0, len(list(sorted_dict.keys())), 10))
    plt.ylabel("How Are They Doing?")
    file_directory = os.path.join(os.path.dirname(__file__), 'static/images/')
    plt.savefig(os.path.join(file_directory, 'user_data_admin.png'))

def getHighRisk():
    
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "EmberitePass2234",
    database = "emberiteDatabase"
    )

    mycursor = db.cursor()
    mycursor.execute("SELECT userID from userTable")

    newDict = dict()
    for x in mycursor:
        id = x
        temp = healthLogic.HealthLogic(id)
        newDict.update(id, temp.getHealthMonthAverage(id))
    
    sortedDict = sorted(newDict.items(), key=lambda item: item[1])
    return {k: sortedDict[k] for k in list(sortedDict)[:4]}