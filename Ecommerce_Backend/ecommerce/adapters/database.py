import pymongo

class DBConnection:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://Pragati:pragati@ecommerce.rrbuh.mongodb.net/ecom?retryWrites=true&w=majority"
        )
        self.db = self.client.ecom

    # def __del__(self):
    #     if self.client and self.client.close:
    #         self.client.close()

    def createUser(self, user):
        data = {
            "user_name": user.getUserName(),
            "email_id": user.getEmail(),
            "contact": user.getContact(),
            "auth_id": user.getAuthId(),
        }
        try:
            self.db.users.insert_one(data)
        except Exception as e:
            print(e)

    def getUser(self, email, contact):
        myquery = {"email_id": email, "contact": contact}
        res = None
        try:
            res = self.db.users.find_one(myquery)
        except Exception as e:
            print(e)
        return res

    def getUserByEmail(self, email):
        myquery = {"email_id": email}
        res = None
        try:
            res = self.db.users.find_one(myquery)
        except Exception as e:
            print(e)
        return res

    def getUserById(self, auth_id):
        myquery = {"auth_id": auth_id}
        res = None
        try:
            res = self.db.users.find_one(myquery)
        except Exception as e:
            print(e)
        return res    

    def getAuthById(self, auth_id):
        myquery = {"auth_id": auth_id}
        res = None
        try:
            res = self.db.auth.find_one(myquery)
        except Exception as e:
            print(e)
        return res        

    def createAuth(self,auth):
        data = {
            "auth_id": auth.getAuthId(),
            "password": auth.getPassword(),
            "role": auth.getRole(),
        }
        try:
            self.db.auth.insert_one(data)
        except Exception as e:
            print(e)
    def updateAuth(self,auth):

        myquery = {"auth_id": auth.getAuthId()}
        updateCol = {"password": auth.getPassword()}
        newvalues = {"$set": updateCol}

        try:
            self.db.auth.update_one(myquery, newvalues)
        except Exception as e:
            print(e)

    def createProduct(self,item):
        item = {
            "product_id": item.product_id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "stock": item.stock,
            "status": item.status
        }
        try:
            self.db.products.insert_one(item)
        except Exception as e:
            print(e)

    def updateProductInfo(
        self, p_id, description=None, price=None, stock=None, status=None
    ):
        myquery = {"product_id": p_id}
        updateCol = {}

        if description != None:
            updateCol["description"] = description
        if price != None:
            updateCol["price"] = price
        if stock != None:
            updateCol["stock"] = stock
        if status != None:
            updateCol["status"] = status

        newvalues = {"$set": updateCol}
        try:
            self.db.products.update_one(myquery, newvalues)
        except Exception as e:
            print(e)

    def getProductById(self, p_id):
        myquery = {"product_id": p_id}
        res = None
        try:
            res = self.db.products.find_one(myquery,{ "_id": 0})
        except Exception as e:
            print(e)
        return res

    def getAllProducts(self):
        mylist = []
        try:
            for d in self.db.products.find({},{ "_id": 0}):
                mylist.append(d)
    
        except Exception as e:
            print(e)
        return mylist

    def createOrder(self, order):
        item = {
            "order_id":order.order_id,
            "product_id": order.product_id,
            "auth_id": order.auth_id,
            "timestamp": order.timestamp,
            "price": order.price,
            "status": order.status
        }
        try:
            self.db.orders.insert_one(item)

        except Exception as e:
            print(e)

    def updateOrderStatus(
        self, o_id, status=None
    ):
        myquery = {"order_id": o_id}
        updateCol = {}
        if status != None:
            updateCol["status"] = status

        newvalues = {"$set": updateCol}
        try:
            self.db.orders.update_one(myquery, newvalues)
        except Exception as e:
            print(e)            


    def getAllOrders(self):
        mylist = []
        try:
            for d in self.db.orders.find({},{ "_id": 0}):
                mylist.append(d)
    
        except Exception as e:
            print(e)
        return mylist

    def getAllOrdersByUserId(self, auth_id):
        myquery = {"auth_id": auth_id}
        mylist = []

        try:
            for d in self.db.orders.find(myquery,{ "_id": 0}):
                mylist.append(d)
        except Exception as e:
            print(e)
        return mylist      

    def getOrderByOrderId(self, order_id):
        myquery = {"order_id": order_id}

        try:
            res=self.db.orders.find_one(myquery,{ "_id": 0})
            
        except Exception as e:
            print(e)
        return res            

    def getOrderByUserAndProductId(self, auth_id , product_id):
        myquery = {"auth_id": auth_id ,"product_id": product_id }
        res = None
        try:
            temp=list(self.db.orders.find(myquery,{ "_id": 0}).sort([("timestamp",-1)]))
            if len(temp) >0:
                res=temp[0]
        except Exception as e:
            print(e)
        return res             