from getpass import getpass
from models.users import userModel
from utils.clear_terminal import clear


def signIn():
    clear()
    name = input('Nome: ')
    document = input('CPF: ')
    password = getpass('Senha: ')

    error = userModel.createUser(name, document, password)

    if(error):
        return False

    return {
        'name': name,
        'document': document,
        'password': password
    }


def logIn():
    clear()

    document = input('CPF: ')
    password = getpass('Senha: ')

    return userModel.checkLogin(document=document, password=password)
