class Questionnaire:
    
    def __init__(self, id, date):
        self.user_id = id
        self.date = date
        self.responses = []
    
    @classmethod
    def get_id(self):
        return self.user_id
    
    def get_date(self):
        return self.date
    
    def get_question_response(self, i):
        return self.responses[i]
    
    def set_question_response(self, answer):
        self.responses.append(answer)
