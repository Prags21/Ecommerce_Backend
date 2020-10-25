from .factories import UserFactory
from .factories import ProductFactory
from .factories import AuthFactory
from ..adapters.UidGenerator import UidGenerator
from ..adapters import validator
from ..adapters import Encrypt
from .product import ProductStatus

Status = ProductStatus

UID = UidGenerator.getInstance()
UserCreator = UserFactory(UID, validator)
ProductCreator = ProductFactory(UID, validator)
AuthCreator = AuthFactory(Encrypt)

#print(UserCreator)
