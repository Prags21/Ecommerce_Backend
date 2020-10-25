from ..entities import ProductCreator

class AddProductUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def addProduct(self, name, description, price, stock,status, token):
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