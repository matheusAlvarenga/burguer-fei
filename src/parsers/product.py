def stringToProduct(string):
    product_array = string.strip().split(',')

    return {
        'id': product_array[0],
        'name': product_array[1],
        'price': product_array[2]
    }
