import enum


class OrderStatus:
    Accepted = "ACCEPTED"
    Delivered = "DELIVERED"
    Cancelled ="CANCELLED"
    Placed = "PLACED"


class Order:
    def __init__(self, order_id, auth_id, product_id, price:int, timestamp, status:OrderStatus):
        self.product_id = product_id
        self.auth_id = auth_id
        self.order_id = order_id
        self.price = price
        self.timestamp = timestamp
        self.status = OrderStatus.Placed
        self.setStatus(status)

    def getProduct_id(self):
        return self.product_id

    def getOrder_id(self):
        return self.order_id

    def getProductPrice(self):
        return self.price

    def getTimestamp(self):
        return self.timestamp

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        if str(status) == str(OrderStatus.Accepted) or str(status) == str(OrderStatus.Delivered) or str(status) == str(OrderStatus.Cancelled) or str(status) == str(OrderStatus.Placed):
            self.status = status
        else:
            raise Exception('Invalid Order status Exception')

