from ..adapters.database import DBConnection
from ..adapters import Tokenize
from .addUser import AddUserUseCase
from .addProduct import AddProductUseCase

conn = DBConnection()
AddUser = AddUserUseCase(conn)
AddProduct = AddProductUseCase(conn)



