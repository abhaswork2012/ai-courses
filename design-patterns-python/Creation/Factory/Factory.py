from abc import ABC,abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza:
    def prepare(self):
        print("Preparing Pizza")
        
class Burger:
    def prepare(self):
        print("Preparing Burger")
        
class FoodFactory:
    @staticmethod
    def create_food(food_type:str) -> Food:
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        else:
            return None
        
class RestaurantService:
    def create_order(self,food_type):
        p = FoodFactory.create_food(food_type)
        p.prepare()
        return p

res = RestaurantService()
p = res.create_order("pizza")
b = res.create_order("burger")