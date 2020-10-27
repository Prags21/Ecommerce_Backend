from ..useCases import AddUser
from .registerUsers import RegisterUser
from ..useCases import AddProduct
from ..useCases import AccessValidation
from .registerProducts import RegisterProduct
from .authController import AuthController
from ..useCases import GetToken
from .updateProducts import UpdateProducts
from ..useCases import UpdateProduct
from .viewProduct import ViewProducts
from ..useCases import ViewProduct
from .orderProduct import OrderProducts
from ..useCases import OrderProduct
from .viewMyOrders import ViewMyOrders
from ..useCases import ViewMyOrder
from .updateOrderStatus import UpdateStatus
from ..useCases import UpdateOrderStatus
from .viewAllOrder import ViewAllOrders
from ..useCases import ViewAllOrder



RegisterUserController= RegisterUser(AddUser, AccessValidation)
RegisterProductController= RegisterProduct(AddProduct,AccessValidation)
UpdateProductController= UpdateProducts(UpdateProduct,AccessValidation)
ViewProductsController = ViewProducts(ViewProduct,AccessValidation)
AuthUserController = AuthController(GetToken)
OrderProductsController = OrderProducts(OrderProduct,AccessValidation)
MyOrdersController= ViewMyOrders(ViewMyOrder,AccessValidation)
UpdateOrderStatusController = UpdateStatus(UpdateOrderStatus,AccessValidation)
AllOrdersController = ViewAllOrders(ViewAllOrder,AccessValidation)