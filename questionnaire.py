class Questionnaire:
    
    def __init__(self, id, date, question_responses):
        self.user_id = id
        self.date = date
        self.respones = question_responses
    
    @classmethod
    def get_id(self):
        return self.user_id
    
    def get_date(self):
        return self.date
    
    def get_question_response(self, i):
        return self.respones[i]
    
    def set_question_response(self, i, answer):
        self.respones[i] = answer
