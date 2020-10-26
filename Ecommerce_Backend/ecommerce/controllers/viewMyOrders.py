class ViewMyOrders:
    def __init__(self,ViewMyOrderUsecase,AccessValidation):
        self.ViewMyOrderUsecase = ViewMyOrderUsecase
        self.AccessValidation = AccessValidation

    def viewAllOrders(self,http_request):
        token = http_request['header']['Authorization']

        auth_info = self.AccessValidation.validate(token)
        auth_id=auth_info['auth_id']

        if not self.ViewMyOrderUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        return self.ViewMyOrderUsecase.viewMyOrder(auth_id)

