from ..entities import UserCreator
from ..entities import AuthCreator

class GetTokenUseCase:
    def __init__(self, db, Tokenize):
        self.db = db
        self.Tokenize = Tokenize
        
    def getToken(self, email, password):
        try:
            user=self.db.getUserByEmail(email)
            if not user:
                raise Exception("Invalid email or password")
            auth = self.db.getAuthById(user['auth_id'])
            if not auth:
                raise Exception("Invalid email or password")    
            temp_auth=AuthCreator.createAuth(password,auth['auth_id'],auth['role'])        
            if not temp_auth.getPassword() ==  auth['password'] :
                raise Exception("Invalid email or password")    
            return self.Tokenize.createToken(temp_auth)

        except Exception as e:
            print(e)
            return {"error": str(e)}
