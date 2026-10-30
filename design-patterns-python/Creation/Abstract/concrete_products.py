from products import Chair, Sofa


class ModernChair(Chair):

    def sit_on(self):
        print("Sitting on a modern chair")


class VictorianChair(Chair):

    def sit_on(self):
        print("Sitting on a Victorian chair")


class ModernSofa(Sofa):

    def lie_on(self):
        print("Lying on a modern sofa")


class VictorianSofa(Sofa):

    def lie_on(self):
        print("Lying on a Victorian sofa")