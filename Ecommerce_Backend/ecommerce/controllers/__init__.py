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






RegisterUserController= RegisterUser(AddUser, AccessValidation)
RegisterProductController= RegisterProduct(AddProduct,AccessValidation)
UpdateProductController= UpdateProducts(UpdateProduct,AccessValidation)
ViewProductsController = ViewProducts(ViewProduct)
AuthUserController = AuthController(GetToken)