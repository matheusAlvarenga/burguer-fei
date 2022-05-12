from getpass import getpass
from models.users import userModel

def signIn():
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
    