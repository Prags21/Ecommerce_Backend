import enum


class ProductStatus:
    Active = "ACTIVE"
    Inactive = "INACTIVE"


class Product:
    def __init__(self, product_id, name, description, price:int, stock:int, status:ProductStatus):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.status = ProductStatus.Inactive
        self.setStatus(status)

    def getProductName(self):
        return self.name

    def getProducrDescription(self):
        return self.description

    def getProductPrice(self):
        return self.price

    def getProductStock(self):
        return self.stock

    def getStatus(self):
        return self.status

    def setPrice(self, newPrice):
        self.price = newPrice

    def setStock(self, newStock):
        self.stock = newStock

    def setStatus(self, status):
        if str(status) == str(ProductStatus.Active) or str(status) == str(ProductStatus.Inactive):
            self.status = status
        else:
            raise Exception('Invalid status Exception')

