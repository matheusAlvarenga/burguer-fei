from classes.database import Database
from parsers.product import stringToProduct


class ProductsModel:
    filePath = 'tmp/products.txt'
    database = Database(filePath)

    def queryProducts(self):
        products = self.database.find()

        for i in range(len(products)):
            products[i] = stringToProduct(products[i])

        return products


productsModel = ProductsModel()
