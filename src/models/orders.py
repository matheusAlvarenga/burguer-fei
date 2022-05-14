from classes.database import Database
from parsers.order import order_to_string, strings_to_orders
from models.products import productsModel


class OrdersModel:
    filePath = 'tmp/orders.txt'
    database = Database(filePath)

    def create_order(self, document, product_id, quantity, action):
        self.database.create(order_to_string(document=document, order={
            'product_id': product_id,
            'quantity': quantity,
            'action': action,
        }))

    def delete_orders(self, query):
        self.database.deleteMany(query)

    def get_users_orders(self, query):
        products = productsModel.queryProducts()

        mapped_orders = []

        orders = self.database.find(query)

        for order in orders:
            mapped_orders.append(strings_to_orders(order, products))

        return mapped_orders


orders_model = OrdersModel()
