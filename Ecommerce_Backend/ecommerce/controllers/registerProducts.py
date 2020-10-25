class RegisterProduct:
    def __init__(self,AddProductUsecase):
        self.AddProductUsecase = AddProductUsecase

    def registerProduct(self,http_request):
        name=http_request['body']['name']
        description=http_request['body']['description']
        price=http_request['body']['price']
        stock=http_request['body']['stock']
        status=http_request['body']['status']
        return self.AddProductUsecase.addProduct(name, description, price, stock,status)

