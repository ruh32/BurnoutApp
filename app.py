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

@app.route('/landingPage', methods=['GET', 'POST'])
def landing_page():
    return render_template('landingPage.html')

@app.route('/journal')
def jounral():
    return render_template('journal.html')

@app.route('/myHealthHistory')
def my_health_history():
    return render_template('myHealthHistory.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == "POST":

        responses = {}
        for i in range(1, 7):
            input_name = f'responses{i}'
            response_value = request.form.get(input_name)
            if response_value is not None:
                responses[f'Question {i}'] = int(response_value)

        if len(responses) == 6:
            return redirect(url_for('landing_page'))
        else:
            return render_template('questions.html')
        

    return render_template('questions.html')

if __name__ == "__main__":
    app.run(debug=True)