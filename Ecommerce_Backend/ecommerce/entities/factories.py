from .users import User
from .product import Product
class UserFactory:
    def __init__(self,UID):
        self.UID=UID

    def createUser(self,name,email,contact):
        auth_id=self.UID.generate()
        user = User(name,email,contact,auth_id) 
        return user


class ProductFactory:
    def __init__(self,UID):
        self.UID=UID

    def createProduct(self,product_info):
        product_id=self.UID.generate()
        item = Product(product_id,product_info.name,product_info.description,product_info.price,product_info.stock,product_info.status) 
        return item        
        
