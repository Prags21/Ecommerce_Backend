from .factories import UserFactory
from ..adapters.UidGenerator import UidGenerator

UID = UidGenerator.getInstance()
UserCreator = UserFactory(UID)
#print(UserCreator)
