from ..entities import Access, ValidateAccess 

class UpdateOrderStatusUseCase:
    def __init__(self, db ,MsgAdapter):
        self.MsgAdapter = MsgAdapter
        self.db = db
        pass

    def validateAccess(self, role):
        required_access_levels = [Access.UPDATE_ORDER_STATUS]
        return ValidateAccess(role, required_access_levels)

    def updateOrderStatus(self, order_id, status):
        #VALIDATION
        item=self.db.getOrderByOrderId(order_id)
        if not item:
            return "No Order exists for given order id"
        else:    
            if item['status'] == status:
                return item
            try:
                self.db.updateOrderStatus(order_id, status)
                updated_item=self.db.getOrderByOrderId(order_id)
                user = self.db.getUserById(updated_item['auth_id'])
                self.MsgAdapter.sendMessage(user['contact'],"Order accepted for order id: "+ order_id)
                return updated_item
            except Exception as e:
                print(e)
                return {"error": str(e)}