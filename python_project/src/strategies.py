from abc import ABC, abstractmethod


class FilterStrategy(ABC):
    @abstractmethod
    def apply(self, row):
        pass


class PriceFilterStrategy(FilterStrategy):
    def __init__(self, min_price):
        self.min_price = min_price

    def apply(self, row):
        return float(row["price"]) >= self.min_price
