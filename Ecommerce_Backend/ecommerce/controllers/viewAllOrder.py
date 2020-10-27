class ViewAllOrders:
    def __init__(self,ViewAllOrderUsecase,AccessValidation):
        self.ViewAllOrderUsecase = ViewAllOrderUsecase
        self.AccessValidation = AccessValidation

    def viewAllOrders(self,http_request):
        token = http_request['header']['Authorization']

        auth_info = self.AccessValidation.validate(token)

        if not self.ViewAllOrderUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        return self.ViewAllOrderUsecase.viewAllOrder()

