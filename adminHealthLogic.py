import user, healthLogic, questionnaire, cgi, datetime, statistics, plotly.express as px, mysql.connector

def getTeamAverage():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "EmberitePass2234",
        database = "emberiteDatabase"
        )

    mycursor = db.cursor()
    mycursor.execute("SELECT userID from questionTable")

    teamAverage = []
    i = 0

    for x in mycursor:
        id = x
        temp = healthLogic.HealthLogic(id)
        teamAverage[i] = temp.getHealthMonthAverage()
        i+=1

    return sum(teamAverage) / len(teamAverage)

