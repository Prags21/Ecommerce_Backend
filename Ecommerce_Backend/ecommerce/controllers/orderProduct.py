class OrderProducts:
    def __init__(self,OrderProductUsecase,AccessValidation):
        self.OrderProductUsecase = OrderProductUsecase
        self.AccessValidation = AccessValidation

    def orderProduct(self,http_request):
        #We can have other route for multiple products to be ordered with one http request.
        product_id=http_request['params']['id']
        token = http_request['header']['Authorization']

        auth_info = self.AccessValidation.validate(token)
        auth_id=auth_info['auth_id']

        if not self.OrderProductUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        return self.OrderProductUsecase.orderProduct(product_id,auth_id)

