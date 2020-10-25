from ..entities import UserCreator

class AddUserUseCase:
    def __init__(self):
        pass
    def addUser(self,name,email,contact):
        try:
            user=UserCreator.createUser(name,email,contact) 
            #store this user in db
            return user.__dict__
        except Exception as e:
            print(e)
            return({"error":"errorssss"})



