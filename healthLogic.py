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
       # df = pd.DataFrame(self.qDict)
        #fig = px.bar(df, x='dates', y='values', title='Mental Health Trends')
        # fig = go.Figure(
        # data=[go.Bar(x=list(self.qDict.keys()), y=list(self.qDict.values()))],
        # layout_title_text="A Figure Displayed with fig.show()"
        # )
        # fig.show() # makes an image
        # div = fig.to_html(full_html=False)
        plt.figure()
        sns.scatterplot(x=list(self.qDict.keys()), y=list(self.qDict.values()))
        # plt.xlabel('Tick')
        # plt.ylabel('Number of keys pressed')
        # plt.title(f'Number of keys pressed in the last 1000-1500 ticks for level {level_key}')
        # plt.show()
        file_directory = os.path.join(os.path.dirname(__file__), 'static/images/')
        print(file_directory)
        plt.savefig(os.path.join(file_directory, 'patient_data.png'))
        # return div
       

    def getHealthMonthAverage(self):
        sortedData = list(reversed(sorted(self.qDict['values'])))
        average = sum(sortedData[:4]) / 4
        return average


    def getHealthDescriptor(self):
        '''healthAverage = self.getHealthMonthAverage()
        if(1 <= healthAverage <= 2): return "Very Good"
        elif(3 <= healthAverage <= 4): return "Good"
        elif(5 <= healthAverage <= 6): return "Ok"
        elif(7 <= healthAverage <= 8): return "Poor"
        else:''' 
        return "Very Poor"
        
    def getHighRisk(self):
        self