class ViewProducts:
    def __init__(self,ViewProductUsecase,AccessValidation):
        self.ViewProductUsecase = ViewProductUsecase
        self.AccessValidation = AccessValidation

    def viewAllProduct(self,http_request):
        token = http_request['header']['Authorization']

        auth_info = self.AccessValidation.validate(token)
        if not self.ViewProductUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        return self.ViewProductUsecase.viewAll()

    def viewAProduct(self,http_request):
        token = http_request['header']['Authorization']
        #from params not body
        body = http_request['body']
        product_id=body['product_id']
        auth_info = self.AccessValidation.validate(token)
        if not self.ViewProductUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        return self.ViewProductUsecase.viewProduct(product_id)    

