from ..useCases import AddUser
from .registerUsers import RegisterUser
from ..useCases import AddProduct
from ..useCases import AccessValidation
from .registerProducts import RegisterProduct
from .authController import AuthController
from ..useCases import GetToken


RegisterUserController= RegisterUser(AddUser, AccessValidation)
RegisterProductController= RegisterProduct(AddProduct)
AuthUserController = AuthController(GetToken)