class Role:
    ADMIN = "ADMIN"
    SALESAGENT = "SALESAGENT"
    CUSTOMER = "CUSTOMER"


class Access:
    CREATE_CUSTOMER = "CREATE_CUSTOMER"
    CREATE_SALES = "CREATE_SALESAGENT"
    ADD_PRODUCT = "ADD_PRODUCT"
    UPDATE_PRODUCT = "UPDATE_PRODUCT"
    VIEW_ORDERS = "VIEW_ORDERS"
    UPDATE_ORDER_STATUS = "UPDATE_ORDER_STATUS"
    SEND_MESSAGE = "SEND_MESSAGE"
    PLACE_ORDER = "PLACE_ORDER"


AccessMap = {
    Role.ADMIN: [
        Access.CREATE_CUSTOMER,
        Access.CREATE_SALES,
        Access.ADD_PRODUCT,
        Access.UPDATE_PRODUCT,
    ],
    Role.SALESAGENT: [
        Access.VIEW_ORDERS,
        Access.UPDATE_ORDER_STATUS,
        Access.SEND_MESSAGE,
    ],
    Role.CUSTOMER: [Access.PLACE_ORDER],
}


class Auth:
    def __init__(self, password, auth_id, role):
        self.password = password
        self.auth_id = auth_id
        self.role = role

    def getPassword(self):
        return self.password

    def getRole(self):
        return self.role

    def getAuthId(self):
        return self.auth_id
