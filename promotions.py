import rom as rom
from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = product.price * self.percent / 100
        total_price = product.price * quantity - discount * quantity
        return total_price


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        total_price = (product.price * full_price_items) + (product.price * 0.5 * half_price_items)
        return total_price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        paid_items = quantity - (quantity // 3)
        total_price = product.price * paid_items
        return total_price
