from ..useCases.addUser import AddUserUseCase
from .registerUsers import RegisterUser

RegisterUserController= RegisterUser(AddUserUseCase())