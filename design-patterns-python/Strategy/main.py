from diwali import DiwaliStrategy
from holi import HoliStrategy
from discount_service import DiscountService
from discount_strategy import DiscountStrategy

diwali_strategy = DiwaliStrategy()
holi_strategy = HoliStrategy()

discount_service = DiscountService(diwali_strategy)
discount_service.process_discount()
discount_service = DiscountService(holi_strategy)
discount_service.process_discount()