from ..entities import Access, ValidateAccess 

class ViewMyOrderUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def validateAccess(self, role):
        required_access_levels = [Access.VIEW_MYORDER]
        return ValidateAccess(role, required_access_levels)

    def viewMyOrder(self,auth_id):
        #VALIDATION
        try:
            order=self.db.getAllOrdersByUserId(auth_id)
            if not order:
                return "No orders placed yet!"
            else: 
                return order
        except Exception as e:
            print(e)
            return {"error": str(e)}   