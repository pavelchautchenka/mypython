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

