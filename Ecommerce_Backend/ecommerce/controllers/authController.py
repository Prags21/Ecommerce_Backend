class AuthController:
    def __init__(self,GetTokenUseCase):
        self.GetTokenUseCase = GetTokenUseCase

    def fetchToken(self,http_request):
        email=http_request['body']['email']
        password=http_request['body']['password']
        return self.GetTokenUseCase.getToken(email,password)

