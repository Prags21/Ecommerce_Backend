from .database import DBConnection
from .Validator import Validator
from .Encrypt import Encrypt
from .Tokenize import TokenGenerator

validator = Validator
Tokenize = TokenGenerator.getInstance()
DBConn=DBConnection()
