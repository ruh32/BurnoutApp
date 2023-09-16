import user, questionnaire, cgi, datetime, statistics, plotly


class HealthLogic:

    def __init__(self, id):
       self.id = id 
       getQDict = questionnaire.Questionnaire(id)
       self.qDict = getQDict.getDict()
    
    def loadGraph(self, range):
        print(self.qDict)
        self
    
    def getHealthDescriptor(self):
        #hold
        self

    def getHealthMonthAverage(self):
        #hold
        self
    

    
