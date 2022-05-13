def userToString(user):
    return f'{user["document"]},{user["name"]},{user["password"]}'


def stringToUser(string):
    user_array = string.strip().split(',')

    return {
        'document': user_array[0],
        'name': user_array[1],
        'password': user_array[2]
    }
