from classes.database import Database
from parsers.order import order_to_string


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


orders_model = OrdersModel()
