from utils.clear_terminal import clear
from printers.table import print_table


def print_orders(orders):
    product_array = []

    mapped_products = list(map(lambda product: {
        'id': product['id'],
        'product_name': product['product_name'],
        'product_price': product['product_price'],
        'quantity': product['quantity'],
        'total_price': product['total_price']
    }, orders))

    for product in mapped_products:
        product_array.append(list(product.values()))

    headers = [
        "Código",
        "Produto",
        "Preço Unitário",
        "Quantidade",
        "Preço Total"
    ]

    clear()

    print(
        'Digite o código do produto que você deseja remover ou 0 para cancelar: '
    )

    print()

    print_table(headers=headers, body=product_array)

    print()

    return input('Código: ')
