from factory import FurnitureFactory
from concrete_products import (
    ModernChair,
    ModernSofa,
    VictorianChair,
    VictorianSofa
)


class ModernFurnitureFactory(FurnitureFactory):

    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):

    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()