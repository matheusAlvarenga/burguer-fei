from utils.find_one_in_array import find_one_in_array


def order_to_string(document, order):
    return f'{document},{order["product_id"]},{order["quantity"]},{order["action"]}'


def strings_to_orders(string, products):
    order_array = string.strip().split(',')

    product = find_one_in_array(
        products,
        lambda product: product['id'] == order_array[1]
    )

    return {
        'id': product['id'],
        'document': order_array[0],
        'product_id': order_array[1],
        'quantity': int(order_array[2]),
        'action': order_array[3],
        'product_price': product['price'],
        'product_name': product['name'],
        'total_price': float(product['price']) * float(order_array[2])
    }
