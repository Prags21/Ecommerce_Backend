from ..adapters.database import DBConnection
from ..adapters import Tokenize
from .addUser import AddUserUseCase
from .addProduct import AddProductUseCase
from .getToken import GetTokenUseCase
from .accessValidator import AccessValidator

conn = DBConnection()
AddUser = AddUserUseCase(conn)
AddProduct = AddProductUseCase(conn)
GetToken = GetTokenUseCase(conn,Tokenize)
AccessValidation = AccessValidator(conn, Tokenize)



