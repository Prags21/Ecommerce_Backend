class UpdateProducts:
    def __init__(self,UpdateProductUsecase,AccessValidation):
        self.UpdateProductUsecase = UpdateProductUsecase
        self.AccessValidation = AccessValidation

    def updateProduct(self,http_request):
        body = http_request['body']
        product_id=body['product_id']
        description=body.get('description')
        price=body.get('price')
        stock=body.get('stock')
        status=body.get('status')
        token = http_request['header']['Authorization']

        auth_info = self.AccessValidation.validate(token)
        if not self.UpdateProductUsecase.validateAccess(auth_info['role']):
            raise Exception("Access Denied")
        return self.UpdateProductUsecase.updateProductInfo(product_id, description, price, stock,status)

