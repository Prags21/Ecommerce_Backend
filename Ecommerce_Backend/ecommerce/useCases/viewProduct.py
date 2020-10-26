from ..entities import Access, ValidateAccess 
from ..entities import ProductCreator

class ViewProductUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def validateAccess(self, role):
        required_access_levels = [Access.ADD_PRODUCT]
        return ValidateAccess(role, required_access_levels)

    def viewAll(self):
        #VALIDATION
        #item=self.db.getAllProducts()
        #if not item:
        #    return "No Product exists in Collection"
        try:
            items=self.db.getAllProducts()
            
            return items
        except Exception as e:
            print(e)
            return {"error": str(e)}

    def viewProduct(self,product_id):
        #VALIDATION
        try:
            item=self.db.getProductById(product_id)
            if not item:
                return "No Product exists for given product id"
            else:  
                return item.__dict__
        except Exception as e:
            print(e)
            return {"error": str(e)}                