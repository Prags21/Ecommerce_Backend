from ..entities import Access, ValidateAccess 
from ..entities import OrderCreator

class OrderProductUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def validateAccess(self, role):
        required_access_levels = [Access.PLACE_ORDER]
        return ValidateAccess(role, required_access_levels)

    def orderProduct(self,product_id,auth_id):
        item=self.db.getProductById(product_id)
        if item['status']!="ACTIVE":
            return "Product OUT OF STOCK!!!"
        else:    
            try:
                status = "PLACED"
                order = OrderCreator.createOrder(auth_id, product_id, item['price'], None, status)
                self.db.createOrder(order)
                stock_k=item['stock']-1
                #print(stock_k)
                self.db.updateProductInfo(product_id,stock=stock_k)
                return order.__dict__
            except Exception as e:
                print(e)
                return {"error": str(e)}