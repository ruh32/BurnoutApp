import user, healthLogic, questionnaire, cgi, datetime, statistics, plotly.express as px, mysql.connector

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
    
    sorted_keys = sorted(newDict.keys(), key=lambda x: int(x[3:]))
    highest_indexed_keys = sorted_keys[-4:]
    monthDict = {key: newDict[key] for key in highest_indexed_keys}

    fig = px.bar(monthDict, x='Time', y='Mental Health', title='Mental Health Trends')
    # fig.show()
    fig.write_image("static/image/plot.jpeg", format="jpeg", width=200, height=300) # makes an image

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