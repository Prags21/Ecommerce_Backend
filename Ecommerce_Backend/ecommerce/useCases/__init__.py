from ..adapters.database import DBConnection
from ..adapters import Tokenize
from .addUser import AddUserUseCase
from .addProduct import AddProductUseCase
from .updateProduct import UpdateProductUseCase
from .getToken import GetTokenUseCase
from .accessValidator import AccessValidator
from .viewProduct import ViewProductUseCase


conn = DBConnection()
AddUser = AddUserUseCase(conn)
AddProduct = AddProductUseCase(conn)
UpdateProduct = UpdateProductUseCase(conn)
ViewProduct = ViewProductUseCase(conn)
GetToken = GetTokenUseCase(conn,Tokenize)
AccessValidation = AccessValidator(conn, Tokenize)



