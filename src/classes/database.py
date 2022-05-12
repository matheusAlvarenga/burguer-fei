class Database:
    def __init__(self, filePath):
        self.filePath = filePath

    def create(self, data):
        with open(self.filePath, mode='a') as database_file:
            database_file.write(data + '\n')
        print('created')

    def delete(self):
        print('deleted')

    def findOne(self):
        print('found')
    