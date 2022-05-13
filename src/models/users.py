from classes.database import Database
from parsers.user import stringToUser, userToString


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

    def checkLogin(self, document, password):
        user_result = self.database.findOne(f'^{document},')

        if(not user_result):
            return False
        else:
            user = stringToUser(user_result)
            if(user['password'] == password):
                return user


userModel = UserModel()
