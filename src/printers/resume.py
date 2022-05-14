from printers.table import print_table
from utils.clear_terminal import clear


def print_resume(user, orders, total_price):
    clear()
    print('Nome:', user['name'])
    print('CPF:', user['document'])
    print('Total: R$', total_price)
    print('Itens do pedido:')

    product_array = []

    mapped_products = list(map(lambda product: {
        'id': product['id'],
        'product_name': product['product_name'],
        'product_price': 'R$' + str(product['product_price']),
        'quantity': product['quantity'],
        'total_price': ('-' if product['action'] == '-' else '+')
        + ' R$ ' + str(product['total_price']),
        'action': 'Cancelado' if product['action'] == '-' else 'Adicionado'
    }, orders))

    for product in mapped_products:
        product_array.append(list(product.values()))

    headers = [
        "Código",
        "Produto",
        "Preço Unitário",
        "Quantidade",
        "Preço Total",
        "Ação"
    ]

    print_table(headers=headers, body=product_array)
