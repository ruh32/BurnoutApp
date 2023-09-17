import user, questionnaire, cgi, datetime, statistics, plotly.express as px, pandas as pd
import plotly.io as pio
import plotly.graph_objs as go
import os
import matplotlib.pyplot as plt
import seaborn as sns

class HealthLogic:

    def __init__(self, id):
       self.id = id 
       getQDict = questionnaire.Questionnaire(id)
       self.qDict = getQDict.getDict()
    
    def createGraph(self):

        sorted_dict = dict(reversed(sorted(self.qDict.items())))
        shrunken_dict = dict(reversed(list(sorted_dict.items())[:5]))
        for key in shrunken_dict:
            shrunken_dict[key] /= 100000

        plt.figure()
        plt.title("User Mental Health Data Over the Last Five Responses")
        sns.lineplot(x=list(shrunken_dict.keys()), y=list(shrunken_dict.values())).invert_yaxis()
        plt.xlabel("Date")
        plt.ylabel("How Am I Doing?")
        file_directory = os.path.join(os.path.dirname(__file__), 'static/images/')
        plt.savefig(os.path.join(file_directory, 'user_data.png'))
       

    def getHealthMonthAverage(self):
        sorted_dict = dict(reversed(sorted(self.qDict.items())))
        shrunken_dict = dict(reversed(list(sorted_dict.items())[:5]))
        average = sum(shrunken_dict.values()) / 4
        return average


    def getHealthDescriptor(self):
        healthAverage = self.getHealthMonthAverage()
        if(1 <= healthAverage <= 2): return "Very Good"
        elif(3 <= healthAverage <= 4): return "Good"
        elif(5 <= healthAverage <= 6): return "Ok"
        elif(7 <= healthAverage <= 8): return "Poor"
        else:
            return "Very Poor"
        
    def getHighRisk(self):
        self