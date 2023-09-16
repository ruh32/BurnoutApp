import user, questionnaire, cgi, datetime, statistics, plotly.express as px


class HealthLogic:

    def __init__(self, id):
       self.id = id 
       getQDict = questionnaire.Questionnaire(id)
       self.qDict = getQDict.getDict()
    
    def createGraph(self, dateRange):
        print(self.qDict) #dictionary of data for user date = key, value = 6 ints from questions
        fig = px.bar(self.qDict, x='Time', y='Mental Health', title='Mental Health Trends')
        # fig.show()
        fig.write_image("static/image/plot.jpeg", format="jpeg", width=200, height=300) # makes an image
       
    def getHealthMonthAverage(self):
        sortedData = dict(reversed(sorted(self.qDict.items(), key=lambda item: item[0])))
        average = sum(list(sortedData.values())[:4]) / 4
        return average


    def getHealthDescriptor(self):
        healthAverage = self.getHealthMonthAverage()
        if(1 <= healthAverage <= 2): return "Very Good"
        elif(3 <= healthAverage <= 4): return "Good"
        elif(5 <= healthAverage <= 6): return "Ok"
        elif(7 <= healthAverage <= 8): return "Poor"
        else: return "Very Poor"
    
    def getHealthMonth(self):
        self

    def createTeamGraph(self):
        self
        createGraph();

    def getHighRisk(self):
        self

    




