from ..entities import UserCreator
from ..entities import AuthCreator
from ..entities import Access, ValidateAccess 
import traceback

class AddUserUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def validateAccess(self, role):
        required_access_levels = [Access.CREATE_CUSTOMER, Access.CREATE_SALESAGENT]
        return ValidateAccess(role, required_access_levels)

    def addUser(self, name, email, contact, password, role):
        try:
            # Creates object of User Entity
            user = UserCreator.createUser(name, email, contact)
            auth = AuthCreator.createAuth(password, user.getAuthId(), role)
            res = self.db.getUser(email, contact)           
            #print(res)
            if not res:
                # store this user in db
                self.db.createUser(user)
                self.db.createAuth(auth)
            return user.__dict__
        except Exception as e:
            traceback.print_exc()
            return {"error": str(e)}
