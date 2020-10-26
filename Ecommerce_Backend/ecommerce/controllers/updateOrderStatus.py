class UpdateStatus:
    def __init__(self,UpdateOrderStatusUsecase,AccessValidation):
        self.UpdateOrderStatusUsecase = UpdateOrderStatusUsecase
        self.AccessValidation = AccessValidation

    def updateStatus(self,http_request):

        status=http_request['body']['status']

        order_id=http_request['params']['id']

        token = http_request['header']['Authorization']

        auth_info = self.AccessValidation.validate(token)
        if not self.UpdateOrderStatusUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        return self.UpdateOrderStatusUsecase.updateOrderStatus(order_id, status)

