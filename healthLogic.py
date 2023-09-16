import user
import questionnaire
import cgi
import datetime
import statistics

def new_questionnaire_responses(user_id):

    form = cgi.FieldStorage()
    new_questionnaire = questionnaire.Questionnaire(user_id, datetime.date.today())
    q1_response = form.getvalue('question_1')
    new_questionnaire.set_question_response(q1_response)
    q2_response = form.getvalue('question_2')
    new_questionnaire.set_question_response(q2_response)
    q3_response = form.getvalue('question_3')
    new_questionnaire.set_question_response(q3_response)
    q4_response = form.getvalue('question_4')
    new_questionnaire.set_question_response(q4_response)
    q5_response = form.getvalue('question_5')
    new_questionnaire.set_question_response(q5_response)
    q6_response = form.getvalue('question_6')
    new_questionnaire.set_question_response(q6_response)

# def calc_monthly_average_health_score(user_id):
#     # need some way to get object out of database with user_id
#     return statistics.mean()
