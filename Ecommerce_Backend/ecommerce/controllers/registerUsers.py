class RegisterUser:
    def __init__(self,AddUserUsecase):
        self.AddUserUsecase = AddUserUsecase

    def registerUser(self,http_request):
        name=http_request['body']['name']
        email=http_request['body']['email']
        contact=http_request['body']['contact']
        password=http_request['body']['password']
        role=http_request['body']['role']

        return self.AddUserUsecase.addUser(name,email,contact,password,role)

