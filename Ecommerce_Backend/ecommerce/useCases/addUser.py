from ..entities import UserCreator
from ..entities import AuthCreator


class AddUserUseCase:
    def __init__(self, db):
        self.db = db
        pass

    def addUser(self, name, email, contact, password, role):
        try:
            # Creates object of User Entity
            user = UserCreator.createUser(name, email, contact)
            auth = AuthCreator.createAuth(password, user.getAuthId(), role)
            res = self.db.getUser(email, contact)
            #TODO insert auth in database
            
            if not res:
                self.db.createUser(user)
            # store this user in db
            return user.__dict__
        except Exception as e:
            print(e)
            return {"error": str(e)}
