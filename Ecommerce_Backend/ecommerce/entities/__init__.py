from .factories import UserFactory
from .factories import ProductFactory
from .factories import AuthFactory
from .factories import OrderFactory
from ..adapters.UidGenerator import UidGenerator
from ..adapters import validator
from ..adapters import Encrypt
from .product import ProductStatus
from .auth import Access, ValidateAccess
from .order import OrderStatus

Status = ProductStatus
OrderStatus= OrderStatus
UID = UidGenerator.getInstance()
UserCreator = UserFactory(UID, validator)
ProductCreator = ProductFactory(UID, validator)
AuthCreator = AuthFactory(Encrypt)
OrderCreator = OrderFactory(UID, validator)
