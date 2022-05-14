from models.products import productsModel
from printers.orders import print_orders
from printers.product import print_products
from models.orders import orders_model
from utils.clear_terminal import clear
from utils.find_one_in_array import find_one_in_array


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


def deleteOrder(document):
    orders_model.delete_orders(f'^{document},')

    print()

    print('Pedido deletado com sucesso.')


def deleteProductInOrder(user):
    orders = orders_model.get_users_orders(f'^{user["document"]},')
    merged_orders = mergeProductsInOrders(orders)

    selected_product = print_orders(merged_orders['merged_orders'])

    if(selected_product != '0'):
        if(selected_product in merged_orders['orders_id']):
            quantity = input(
                "Quantos items desse produto você deseja cancelar? "
            )

            if(int(quantity) <= int(find_one_in_array(
                merged_orders['merged_orders'],
                lambda order: order['id'] == selected_product
            )['quantity'])):
                orders_model.create_order(
                    document=user['document'],
                    quantity=quantity,
                    product_id=selected_product,
                    action='-'
                )

                return True

            else:
                clear()
                print('Impossível cancelar essa quantidade.')

        else:
            clear()
            print('Produto não encontrado no seu pedido.')

    return False


def mergeProductsInOrders(orders):
    orders_id = set(list(map(lambda order: order['product_id'], orders)))

    merged_orders = []

    for order_id in orders_id:
        filtered_orders = list(
            filter(
                lambda order: order['id'] == order_id,
                orders
            )
        )

        quantity = 0
        total_price = 0

        for order in filtered_orders:
            if(order['action'] == '+'):
                quantity += order['quantity']
                total_price += order['total_price']
            else:
                quantity -= order['quantity']
                total_price -= order['total_price']

        if(quantity == 0):
            continue

        new_order = filtered_orders[0]

        new_order['quantity'] = quantity
        new_order['total_price'] = total_price

        merged_orders.append(new_order)

    return {
        'merged_orders': merged_orders,
        'orders_id': orders_id
    }


def totalPriceFromOrders(user):
    orders = orders_model.get_users_orders(f'^{user["document"]},')
    merged_orders = mergeProductsInOrders(orders)

    total_price = 0

    for order in merged_orders['merged_orders']:
        total_price += order['total_price']

    return total_price
