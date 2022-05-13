from models.products import productsModel
from printers.product import print_products
from models.orders import orders_model


def createOrder(document):
    all_products = productsModel.queryProducts()

    another_product = True

    while(another_product):
        addProductToOrder(all_products, document)

        print()

        another_product = input(
            'Você deseja adicionar mais um produto? (S/N)'
        ) == 'S'


def addProductToOrder(products, document):
    selected_product = print_products(products)

    quantity = input("Quantos items desse produto você deseja? ")

    orders_model.create_order(
        document=document,
        quantity=quantity,
        product_id=selected_product,
        action='+'
    )
