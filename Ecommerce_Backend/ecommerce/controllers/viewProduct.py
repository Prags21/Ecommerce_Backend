class ViewProducts:
    def __init__(self,ViewProductUsecase,AccessValidation):
        self.ViewProductUsecase = ViewProductUsecase
        self.AccessValidation = AccessValidation

    def viewAllProduct(self,http_request):
        return self.ViewProductUsecase.viewAll()

    def viewAProduct(self,http_request):

        product_id=http_request['params']['id']
        token = http_request['header'].get('Authorization')
        if not token is None:
            auth_info = self.AccessValidation.validate(token)
            return self.ViewProductUsecase.viewProduct(product_id,auth_info['auth_id'])    
        return self.ViewProductUsecase.viewProduct(product_id)
