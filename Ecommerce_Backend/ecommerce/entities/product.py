class Product:
    def __init__(self,product_id,name,description,price,stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.for_sale=for_sale
    
    def getProductName(self):
        return self.name

    def getProducrDescription(self):
        return self.description

    def getProductPrice(self):
        return self.price

    def getProductStock(self):
        return self.stock 

    def getForSale(self):
        return self.for_sale                

    def setPrice(self,newPrice):
        self.price = newPrice   

    def setStock(self,newStock):
        self.stock = newStock 
        
    def setForSaleStatus(self,status):
        self.for_sale = status           