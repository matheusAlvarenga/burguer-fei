from re import findall
from os.path import exists, dirname
from os import makedirs


class Database:
    def __init__(self, filePath):
        self.filePath = filePath
        if(not exists(filePath)):
            makedirs(dirname(filePath), exist_ok=True)
            open(filePath, mode='x')

    def create(self, data):
        with open(self.filePath, mode='a') as database_file:
            database_file.write(data + '\n')
        print('created')

    def delete(self):
        print('deleted')

    def find(self, query=''):
        responses = []

        with open(self.filePath, mode='r') as database_file:
            lines = database_file.readlines()
            for line in lines:
                if(findall(query, line)):
                    responses.append(line)

        return responses

    def findOne(self, query):
        with open(self.filePath, mode='r') as database_file:
            lines = database_file.readlines()
            for line in lines:
                if(findall(query, line)):
                    return line

            return False
