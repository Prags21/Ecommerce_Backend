class User:
    def __init__(self,user_name,email,contact,auth_id):
        self.user_name = user_name
        self.email_id = email
        self.contact = contact
        self.auth_id = auth_id
    
    def getUserName(self):
        return self.user_name

    def getEmail(self):
        return self.email_id

    def getAuthId(self):
        return self.auth_id

    def getContact(self):
        return self.contact
