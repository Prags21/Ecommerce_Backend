class RegisterProduct:
    def __init__(self,AddProductUsecase,AccessValidation):
        self.AddProductUsecase = AddProductUsecase
        self.AccessValidation = AccessValidation

    def registerProduct(self,http_request):
        name=http_request['body']['name']
        description=http_request['body']['description']
        price=http_request['body']['price']
        stock=http_request['body']['stock']
        status=http_request['body']['status']
        token = http_request['header']['Authorization']

        auth_info = self.AccessValidation.validate(token)
        if not self.AddProductUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        return self.AddProductUsecase.addProduct(name, description, price, stock,status)

