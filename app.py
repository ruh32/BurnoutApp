from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/landingPage')
def landing_page():
    return render_template('landingPage.html')

@app.route('/journal')
def jounral():
    return render_template('jounral.html')

@app.route('/myHealthHistory')
def my_health_history():
    return render_template('myHealthHistory.html')

@app.route('/questions')
def questions():
    return render_template('')

if __name__ == "__main__":
    app.run(debug=True)