
class AccessValidator:
    def __init__(self, db, Tokenize):
        self.Tokenize = Tokenize
        self.db = db
        
    def validate(self,token):
        if not token:
            raise Exception("Invalid Token")

        data = self.Tokenize.getData(token)
        if not data:
            raise Exception("Invalid Token")

        auth_info = self.db.getAuthById(data['auth_id'])
        if not auth_info:
            raise Exception("Invalid Token")

        return auth_info
