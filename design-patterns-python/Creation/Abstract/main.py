from concrete_factories import (
    ModernFurnitureFactory,
    VictorianFurnitureFactory
)


def furnish_house(factory):

    chair = factory.create_chair()
    sofa = factory.create_sofa()

    chair.sit_on()
    sofa.lie_on()


print("Modern Furniture:")
furnish_house(ModernFurnitureFactory())

print("\nVictorian Furniture:")
furnish_house(VictorianFurnitureFactory())