class AuthController:
    def __init__(self,GetTokenUseCase):
        self.GetTokenUseCase = GetTokenUseCase

    def fetchToken(self,http_request):
        body = http_request['body']
        email=body.get('email') 
        password=body.get('password') 
        if password == None: 
            return self.GetTokenUseCase.getOTP(email)
        return self.GetTokenUseCase.getToken(email,password)

