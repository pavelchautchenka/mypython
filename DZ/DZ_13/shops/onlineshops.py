from .abstract import AbstractShop
from .typess import Product,  Components, Article
from .errortypes import NonProductError


class Example(AbstractShop):
    def __init__(self):
        self.shop = []

    def add_product(self, product):
        if isinstance(product, Product | Article | Components):
            self.shop.append(product)
        else:
            raise NonProductError(f"The value passed is not a Product class")

    def sell_product(self, product):
        self.shop.remove(product)

    def all_products(self):
        return self.shop


class RealShop(Example):
    pass


class FurnitureShop(Example):
    pass


class ComputerShop(Example):
    pass


class LibraryShop(Example):
    pass