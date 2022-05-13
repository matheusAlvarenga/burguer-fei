from utils.clear_terminal import clear
from printers.table import print_table


def print_products(products):
    product_array = []

    for product in products:
        product_array.append(list(product.values()))

    headers = ["Código", "Produto", "Preço"]

    clear()

    print('Digite o código do produto que você deseja adicionar: ')

    print()

    print_table(headers=headers, body=product_array)

    print()

    return input('Código: ')
