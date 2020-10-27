from ..entities import UserCreator
from ..entities import AuthCreator
import random
class GetTokenUseCase:
    def __init__(self, db, Tokenize ,MessageAdapter):
        self.db = db
        self.MessageAdapter =MessageAdapter
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
            if temp_auth['role'] == "CUSTOMER" :
                empty_auth=AuthCreator.createAuth("",auth['auth_id'],auth['role']) 
                #print(temp_auth.__dict__)       
                self.db.updateAuth(empty_auth) 
            return { "token": self.Tokenize.createToken(temp_auth) }

        except Exception as e:
            print(e)
            return {"error": str(e)}

    def getOTP(self, email):
        try:
            user=self.db.getUserByEmail(email)
            auth = self.db.getAuthById(user['auth_id'])
            if not auth['role'] == "CUSTOMER" :
                raise Exception ("OTP available for customers only.")

            if not user:
                raise Exception("Invalid email or password")
            contact = user['contact']
            password = str(int(random.randrange(1000, 9999, 3)))
            temp_auth=AuthCreator.createAuth(password,auth['auth_id'],auth['role']) 
            #print(temp_auth.__dict__)       
            self.db.updateAuth(temp_auth)
            return self.MessageAdapter.sendMessage(contact,password)

        except Exception as e:
            print(e)
            return {"error": str(e)}