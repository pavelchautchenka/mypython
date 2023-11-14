from .abstract import AbstractShop
from .typess import Product, Check, Components, Article


class RealShop(AbstractShop, Check):
    def __init__(self):
        self.shop = []

    def add_product(self, product: Product):
        if self.validator(product):
            self.shop.append(product)

    def sell_product(self, product: Product):
        self.shop.remove(product)

    def all_products(self):
        return self.shop


class FurnitureShop(AbstractShop, Check):
    def __init__(self):
        self.shop = []

    def add_product(self, product: Product):
        if self.validator(product):
            self.shop.append(product)

    def sell_product(self, product: Product):
        self.shop.remove(product)

    def all_products(self):
        return self.shop


class ComputerShop(AbstractShop, Check):
    def __init__(self):
        self.shop = []

    def add_product(self, product: Components):
        if self.validator(product):
            self.shop.append(product)

    def sell_product(self, product: Components):
        self.shop.remove(product)

    def all_products(self):
        return self.shop


class LibraryShop(AbstractShop, Check):
    def __init__(self):
        self.shop = []

    def add_product(self, product: Article):
        if self.validator(product):
            self.shop.append(product)

    def sell_product(self, product: Article):
        self.shop.remove(product)

    def all_products(self):
        return self.shop
