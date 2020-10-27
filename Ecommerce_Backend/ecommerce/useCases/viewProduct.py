from ..entities import Access, ValidateAccess 

class ViewProductUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def viewAll(self):
        try:
            items=self.db.getAllProducts()
            return items
        except Exception as e:
            print(e)
            return {"error": str(e)}

    def viewProduct(self,product_id,auth_id=None):
        #VALIDATION
        try:
            item=self.db.getProductById(product_id)
            if not item:
                return "No Product exists for given product id"
            if not auth_id is None:    
                last_order=self.db.getOrderByUserAndProductId(auth_id,product_id)
                if not last_order is None:
                    item["last_purchase_price"]=last_order['price']    
            return item
        except Exception as e:
            print(e)
            return {"error": str(e)}                