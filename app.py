from flask import Flask, render_template, request, redirect, url_for
import loginCheck, user

app = Flask(__name__)
current_user = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form.get('uname')
        password = request.form.get('psw')
        checker = loginCheck.LoginCheck()
        if checker.checkValid(username, password):
            current_user = user.User(checker.getUserID(username, password))
            return render_template('landingPage.html')
        
    return render_template('index.html')  

@app.route('/landingPage')
def landing_page():

    if current_user is not None:
        return render_template('landingPage.html')
    else:
        return render_template('index.html')
    

@app.route('/journal')
def journal():
    if current_user is not None:
        return render_template('journal.html')
    else:
        return render_template('index.html')

@app.route('/myHealthHistory')
def my_health_history():
    if current_user is not None:
        return render_template('myHealthHistory.html')
    else:
        return render_template('index.html')

@app.route('/resources')
def resources():
    if current_user is not None:
        return render_template('resources.html')
    else:
        return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if current_user is not None:
        if request.method == "POST":
            responses = {}
            for i in range(1, 7):
                input_name = f'response{i}'
                response_value = request.form.get(f'response{i}')
                print(response_value)
                if response_value is not None:
                    responses[i] = response_value

            if len(responses) == 6:
                # TODO add responses to new questionnaire

                return redirect(url_for('landing_page'))
            else:
                return render_template('questions.html')

        return render_template('questions.html')
    
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)