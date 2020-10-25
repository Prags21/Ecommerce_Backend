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
            res = self.db.products.find_one(myquery)
        except Exception as e:
            print(e)
        return res

    def getAllProducts(self):
        mylist = []
        try:
            for d in self.db.products.find():
                mylist.append(d)
        except Exception as e:
            print(e)
        return mylist



# user=getUserByEmail("abc0")
# auth=getAuthById(user.getAuthId())
# print(auth)