from ..entities import Access, ValidateAccess 

class UpdateProductUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def validateAccess(self, role):
        required_access_levels = [Access.ADD_PRODUCT]
        return ValidateAccess(role, required_access_levels)

    def updateProductInfo(self,product_id, description, price, stock,status):
        #VALIDATION
        item=self.db.getProductById(product_id)
        if not item:
            return "No Product exists for given product id"
        else:    
            try:
                self.db.updateProductInfo(product_id, description, price, stock,status)
                return "Updated successfully"
            except Exception as e:
                print(e)
                return {"error": str(e)}