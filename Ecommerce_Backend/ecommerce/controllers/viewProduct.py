class ViewProducts:
    def __init__(self,ViewProductUsecase):
        self.ViewProductUsecase = ViewProductUsecase

    def viewAllProduct(self,http_request):
        return self.ViewProductUsecase.viewAll()

    def viewAProduct(self,http_request):

        product_id=http_request['params']['id']

        return self.ViewProductUsecase.viewProduct(product_id)    

