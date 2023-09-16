class Resources:

    def __init__(self, name, url, phone_number, logo, desc, active):
        self.name = name
        self.url = url
        self.phone_number = phone_number
        self.logo = logo
        self.desc = desc
        self.active = active

    @classmethod
    def get_name(self):
        return self.name
    
    def get_url(self):
        return self.url
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_logo(self):
        return self.logo
    
    def get_desc(self):
        return self.desc
    
    def get_active_status(self):
        return self.active
