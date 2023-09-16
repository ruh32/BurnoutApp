class Entry:

    def __init__(self, id, date, entry):
        self.user_id = id
        self.date = date
        self.entry = entry

    @classmethod
    def get_id(self):
        return self.user_id
    
    def get_date(self):
        return self.date
    
    def get_entry(self):
        return self.entry
        
    def set_entry(self, new_entry):
        self.entry = new_entry