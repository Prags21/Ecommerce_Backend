from .users import User
from .product import Product
from .auth import Auth

class AuthFactory:
    def __init__(self,Encrypt):
        self.Encrypt=Encrypt

    def createAuth(self,password,auth_id,role):
        auth = Auth(self.Encrypt.cipher(password),auth_id,role) 
        return auth

class UserFactory:
    def __init__(self,UID, Validator):
        self.UID=UID
        self.Validator = Validator

    def createUser(self,name,email,contact):
        auth_id=self.UID.generate()
        if not self.Validator.validateName(name):
            raise Exception('Invalid name')
        if not self.Validator.validateEmail(email):
            raise Exception('Invalid email')
        if not self.Validator.validateContact(contact):
            raise Exception('Invalid contact')
        user = User(name,email,contact,auth_id) 
        return user


class ProductFactory:
    def __init__(self,UID,Validator):
        self.UID=UID
        self.Validator = Validator

    def createProduct(self, name, description, price, stock, status):
        product_id=self.UID.generate()

        if not self.Validator.validateName(name):
            raise Exception('Invalid name')
        if not self.Validator.validateName(description):
            raise Exception('Invalid description')
        if not self.Validator.validateNumber(price):
            raise Exception('Invalid Price')
        if not self.Validator.validateNumber(stock):
            raise Exception('Invalid Stock')

        item = Product(product_id,name,description,price,stock,status) 
        return item        
        
