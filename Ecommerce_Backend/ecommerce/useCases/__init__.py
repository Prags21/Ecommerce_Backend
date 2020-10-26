from ..adapters.database import DBConnection
from ..adapters import Tokenize
from .addUser import AddUserUseCase
from .addProduct import AddProductUseCase
from .updateProduct import UpdateProductUseCase
from .getToken import GetTokenUseCase
from .accessValidator import AccessValidator
from .viewProduct import ViewProductUseCase
from .orderProduct import OrderProductUseCase
from .viewMyOrder import ViewMyOrderUseCase
from .updateOrderStatus import UpdateOrderStatusUseCase
from ..adapters import MessageAdapter

conn = DBConnection()
AddUser = AddUserUseCase(conn)
AddProduct = AddProductUseCase(conn)
UpdateProduct = UpdateProductUseCase(conn)
ViewProduct = ViewProductUseCase(conn)
OrderProduct = OrderProductUseCase(conn)
GetToken = GetTokenUseCase(conn,Tokenize,MessageAdapter)
AccessValidation = AccessValidator(conn, Tokenize)
ViewMyOrder = ViewMyOrderUseCase(conn) 
UpdateOrderStatus = UpdateOrderStatusUseCase(conn,MessageAdapter)



