def order_to_string(document, order):
    return f'{document},{order["product_id"]},{order["quantity"]},{order["action"]}'
