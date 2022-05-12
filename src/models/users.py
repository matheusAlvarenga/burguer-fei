from classes.database import Database
from parsers.user import userToString 

class UserModel:
    filePath = 'tmp/users.txt'
    database = Database(filePath)

    def createUser(self, name, document, password):
        self.database.create(userToString({
            'name': name,
            'document': document,
            'password': password
        }))

userModel = UserModel()