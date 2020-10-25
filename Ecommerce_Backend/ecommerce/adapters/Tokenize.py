import python_jwt as jwt, jwcrypto.jwk as jwk, datetime

class TokenGenerator:
    __instance = None
    
    @staticmethod 
    def getInstance():
      if TokenGenerator.__instance == None:
         TokenGenerator()
      return TokenGenerator.__instance

    def __init__(self):    
        self.key = jwk.JWK.generate(kty='RSA', size=2048)
        if TokenGenerator.__instance != None:
         raise Exception('This class is a singleton!')
        else:
            TokenGenerator.__instance = self

    def createToken(self, auth):
        data = {'auth_id': auth.getAuthId(), 'role': auth.getRole()}
        token = jwt.generate_jwt(data, self.key, 'PS256', datetime.timedelta(hours=24))
        return token

    def getData(self, token):
        header, claims = jwt.verify_jwt(token, self.key, ['PS256'])
        return { 'auth_id': claims['auth_id'], 'role': claims['role']}

