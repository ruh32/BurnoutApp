from flask import Flask, render_template, request, redirect, url_for
import loginCheck, user, questionnaire, datetime, healthLogic, adminHealthLogic
app = Flask(__name__)
current_user = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form.get('uname')
        password = request.form.get('psw')
        checker = loginCheck.LoginCheck()
        if checker.checkValid(username, password):
            global current_user
            current_user = user.User(checker.getUserID(username, password))
            if current_user.get_admin_status():
               return render_template('adminLandingPage.html') 
            else:
                userHealthData = healthLogic.HealthLogic(current_user.id)
                healthDescriptor = userHealthData.getHealthDescriptor()
                return render_template(landingPageRenderTemplate())
        
    return render_template('index.html')  

@app.route('/landingPage', methods=['GET', 'POST'])
def landing_page():
    return render_template(landingPageRenderTemplate())


@app.route('/journal')
def journal():
    return render_template('journal.html')


@app.route('/myHealthHistory', methods=['GET', 'POST'])
def my_health_history():
    return render_template('myHealthHistory.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == "POST":
        responses = []
        for i in range(6):
            input_name = f'response{i+1}'
            response_value = request.form.get(f'response{i+1}')
            print(response_value)
            if response_value is not None:  
                responses.append(int(response_value))

        if len(responses) == 6:

            responseVal = 0
            for i in range(len(responses)):
                    responseVal *= 10
                    responseVal += responses[i]

            print(responseVal)
            global responseClass
            responseClass = questionnaire.Questionnaire(current_user.id)
            responseClass.set_question_response(current_user.id, datetime.datetime.now().date(), responseVal)

            return redirect(url_for('landing_page'))
        else:
            return render_template('questions.html')
    return render_template('questions.html')

@app.route('/adminLandingPage', methods=['GET', 'POST'])
def admin_landing_page():
    return render_template('adminLandingPage.html')

@app.route('/metadata')
def metadata():
    return render_template('metadata.html')

@app.route('/atRisk')
def atRisk():
    atRiskMembers = adminHealthLogic.getHighRisk()
    keys = []
    values = []
    for key, value in atRiskMembers.items():
        keys.append(key)
        values.append(value)
        if len(keys) == 5:
            break
    member1=keys[0]
    memberScore1=values[0]
    member2=keys[1]
    memberScore2=values[1]
    member3=keys[2]
    memberScore3=values[2]
    member4=keys[4]
    memberScore4=values[3]
    member5=keys[5]
    memberScore5=values[4]
    return render_template('atRisk.html', member1=member1, memberScore1=memberScore1, member2=member2, memberScore2=memberScore2, member3=member3, 
                           memberScore3=memberScore3, member4=member4, memberScore4=memberScore4, member5=member5, memberScore5=memberScore5)

@app.route('/userSearch')
def userSearch():
    return render_template('userSearch.html')

@app.route('/resourceLibrary')
def resourceLibrary():
    return render_template('resourceLibrary.html')


def landingPageRenderTemplate():
    userHealthData = healthLogic.HealthLogic(current_user.id)
    '''monthAverage = userHealthData.getHealthMonthAverage()
    healthDescriptor = userHealthData.getHealthDescriptor()'''
    userHealthData.createGraph()
    print("'landingPage.html', score = ")
    return "'landingPage.html', plot_div=  "

if __name__ == "__main__":
    app.run(debug=True)