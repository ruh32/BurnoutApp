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
        fig.write_image("plot.jpeg", format="jpeg", width=800, height=600)
       

    def getHealthMonthAverage(self):
        sorted_data = dict(sorted(self.qDict.items(), key=lambda item: item[0]))
        print(sorted_data)

    def getHealthDescriptor(self):
        #hold
        self
    
    def getHealthMonth(self):
        self

    def createTeamGraph(self):
        self

    def getHighRisk(self):
        self

    




