class ViewProducts:
    def __init__(self,ViewProductUsecase):
        self.ViewProductUsecase = ViewProductUsecase

    def viewAllProduct(self,http_request):
        return self.ViewProductUsecase.viewAll()

    def viewAProduct(self,http_request):
        #token = http_request['header']['Authorization']
        #from params not body
        product_id=http_request['params']['id']
        #auth_info = self.AccessValidation.validate(token)
        #if not self.ViewProductUsecase.validateAccess(auth_info['role']):
            #raise Exception("Access Denied")
        return self.ViewProductUsecase.viewProduct(product_id)    

