import user, questionnaire, cgi, datetime, statistics, plotly.express as px


class HealthLogic:

    def __init__(self, id):
       self.id = id 
       getQDict = questionnaire.Questionnaire(id)
       self.qDict = getQDict.getDict()
    
    def createGraph(self):
        sorted_keys = sorted(self.qDict.keys(), key=lambda x: int(x[3:]))
        highest_indexed_keys = sorted_keys[-4:]
        monthDict = {key: self.qDict[key] for key in highest_indexed_keys}

        fig = px.bar(monthDict, x='Time', y='Mental Health', title='Mental Health Trends')
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
        
    def getHighRisk(self):
        self