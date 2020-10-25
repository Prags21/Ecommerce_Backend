class RegisterUser:
    def __init__(self,AddUserUsecase, AccessValidation):
        self.AddUserUsecase = AddUserUsecase
        self.AccessValidation = AccessValidation

    def registerUser(self,http_request):
        name=http_request['body']['name']
        email=http_request['body']['email']
        contact=http_request['body']['contact']
        password=http_request['body']['password']
        role=http_request['body']['role']

        token = http_request['header']['Authorization']
        auth_info = self.AccessValidation.validate(token)
        print()
        if not self.AddUserUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        
        return self.AddUserUsecase.addUser(name,email,contact,password,role)

