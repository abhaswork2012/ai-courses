from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.__strategy = discount_strategy
    
    def set_strategy(self, discount_strategy: DiscountStrategy):
        self.__strategy = discount_strategy
    
    def process_discount(self):
        return self.__strategy.apply_discount()