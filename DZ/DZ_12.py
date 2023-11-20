from dataclasses import dataclass
from abc import ABC, abstractmethod

class AbstractShop(ABC):

    @abstractmethod
    def add_product(self, product):

        pass

    @abstractmethod
    def sell_product(self, product):
        pass

    @abstractmethod
    def all_products(self):
        pass


class NonProductError(Exception):
    pass


@dataclass
class Product:
    id: int
    name: str
    price: float


@dataclass
class Pizza(Product):
    diameter: int
    spicy: str


@dataclass
class Coffee(Product):
    size: str

@dataclass
class Furniture(Product):
    type: str

@dataclass
class Table(Furniture):
    forme: str


@dataclass
class Chair(Furniture):
    material: str


@dataclass
class Locker(Furniture):
    size: str


class RealShop(AbstractShop):
    def __init__(self):
        self.shop = []

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.shop.append(product)
        else:
            raise NonProductError(f"The value passed is not a Product class")

    def sell_product(self, product: Product):
        self.shop.remove(product)

    def all_products(self):
        return self.shop


class FurnitureShop(AbstractShop):
    def __init__(self):
        self.shop = []

    def add_product(self, product: Table | Chair | Locker):
        if isinstance(product, Product):
            self.shop.append(product)
        else:
            raise NonProductError(f"The value passed is not a Product class")

    def sell_product(self, product: Product):
        self.shop.remove(product)

    def all_products(self):
        return self.shop


coffee1 = Coffee(1225, "cappuccino", 12, 'M')
coffee2 = Coffee(1114, "espresso", 7, "S")
pizza1 = Pizza(122, "margarita", 20, 35, 'with filling')
my_shop = RealShop()
my_shop.add_product(coffee2)
my_shop.add_product(coffee1)
my_shop.add_product(pizza1)
my_shop.sell_product(coffee2)

print(my_shop.all_products())

coffee3 = NameError(1225, "cappuccino", 12, 'M')
my_shop.add_product(coffee3)

fur_shop = FurnitureShop()
table1 = Table(12, "azea", 520, 'big table', 'round')
chair1 = Chair(13, 'sdqdq', 640, 'venge', 'wood')
locker1 = Locker(14, "dqsqd", 760, "steel", 'small')
fur_shop.add_product(table1)
fur_shop.add_product(chair1)
fur_shop.add_product(locker1)
fur_shop.sell_product(locker1)
print(my_shop.all_products())
c = Coffee(125, 'dsdq', 122, "sdqdsd")
fur_shop.add_product(pizza1)
print(my_shop.all_products())


coffee4 = Coffee.id(12154)