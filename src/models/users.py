from classes.database import Database
from parsers.user import userToString 

class UserModel:
    filePath = 'tmp/users.txt'
    database = Database(filePath)

    def createUser(self, name, document, password):
        exists = self.database.findOne(f'^{document},')

        if(not exists):
            self.database.create(userToString({
                'name': name,
                'document': document,
                'password': password
            }))
            return False
        else:
            return True

userModel = UserModel()