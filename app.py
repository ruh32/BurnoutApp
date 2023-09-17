from flask import Flask, render_template, request, redirect, url_for
import loginCheck, user, questionnaire, datetime, healthLogic
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
                return render_template('landingPage.html', score= healthDescriptor)
        
    return render_template('index.html')  

@app.route('/landingPage', methods=['GET', 'POST'])
def landing_page():
    #if current_user is not None:


    userHealthData = healthLogic.HealthLogic(current_user.id)
    monthAverage = userHealthData.getHealthMonthAverage()
    healthDescriptor = userHealthData.getHealthDescriptor()
    print(current_user)
    print(healthDescriptor)


    return render_template('landingPage.html', score="Shit")
    #else:
        #return render_template('index.html')
    

@app.route('/journal')
def journal():
    #if current_user is not None:
        return render_template('journal.html')
    #else:
        #return render_template('index.html')

@app.route('/myHealthHistory', methods=['GET', 'POST'])
def my_health_history():
    #if current_user is not None:



        return render_template('myHealthHistory.html')
    #else:
        #return render_template('index.html')

@app.route('/resources')
def resources():
    #if current_user is not None:
        return render_template('resources.html')
    #else:
        #return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    #if current_user is not None:
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
    #else:
        #return render_template('index.html')

@app.route('/adminLandingPage', methods=['GET', 'POST'])
def admin_landing_page():
    # if current_user is not None:
        return render_template('adminLandingPage.html')
    # else:
       # return render_template(url_for('index.html'))

@app.route('/metadata')
def metadata():
    return render_template('metadata.html')



if __name__ == "__main__":
    app.run(debug=True)