from getpass import getpass
from models.users import userModel

def signIn():
    name = input('Nome: ')
    document = input('CPF: ')
    password = getpass('Senha: ')

    userModel.createUser(name, document, password)

    return {
        'name': name,
        'document': document,
        'password': password
    }
    