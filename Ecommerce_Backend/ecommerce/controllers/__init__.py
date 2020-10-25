from ..useCases import AddUser
from .registerUsers import RegisterUser
from ..useCases import AddProduct
from .registerProducts import RegisterProduct

RegisterUserController= RegisterUser(AddUser)
RegisterProductController= RegisterProduct(AddProduct)