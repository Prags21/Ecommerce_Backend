from ..entities import ProductCreator
from ..entities import Access, ValidateAccess 

class AddProductUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def validateAccess(self, role):
        required_access_levels = [Access.ADD_PRODUCT]
        return ValidateAccess(role, required_access_levels)

    def addProduct(self, name, description, price, stock,status):
        #VALIDATION
        try:
            # Creates object of Product Entity
            item = ProductCreator.createProduct(name, description, price, stock, status)
            self.db.createProduct(item)
            # store this product in db
            return item.__dict__
        except Exception as e:
            print(e)
            return {"error": str(e)}