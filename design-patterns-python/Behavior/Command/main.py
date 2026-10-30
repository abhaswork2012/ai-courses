from chef import Chef
from burger_order import BurgerOrder
from pizza_order import PizzaOrder
from waiter import Waiter

chef = Chef()
burgerOrder = BurgerOrder(chef)
pizza_order = PizzaOrder(chef)
waiter = Waiter()

waiter.take_order(burgerOrder)