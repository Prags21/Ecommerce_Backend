from ..entities import Access, ValidateAccess 

class ViewAllOrderUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def validateAccess(self, role):
        required_access_levels = [Access.VIEW_ORDERS]
        return ValidateAccess(role, required_access_levels)

    def viewAllOrder(self):
        try:
            order=self.db.getAllOrders()
            if not order:
                return "Order Collection Empty!"
            else: 
                return order
        except Exception as e:
            print(e)
            return {"error": str(e)}   