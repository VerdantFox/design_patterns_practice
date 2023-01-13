"""Decorator pattern: Starbuzz coffee example."""


class Beverage:

    def __init__(self) -> None:
        self.description = None

    def get_description(self):
        return self.description

    def cost(self):
        raise NotImplementedError("Implement this...")


class HouseBlend(Beverage):

    def __init__(self) -> None:
        super().__init__()
        self.description = "House blend coffee"

    def cost(self):
        return 1.10


class DarkRoast(Beverage):

    def __init__(self) -> None:
        super().__init__()
        self.description = "Dark Roast coffee"

    def cost(self):
        return 0.75


class Espresso(Beverage):

    def __init__(self) -> None:
        super().__init__()
        self.description = "Espresso coffee"

    def cost(self):
        return 2.10


class Decaf(Beverage):

    def __init__(self) -> None:
        super().__init__()
        self.description = "Decaf coffee"

    def cost(self):
        return 1.25


class CondimentDecorator(Beverage):

    def __init__(self, beverage) -> None:
        self.beverage = beverage
        self.description = ""

    def get_description(self):
        self.beverage.description += f" + {self.description}"
        return self.beverage.get_description()

    def cost(self):
        raise NotImplementedError("Implement this for each...")


class Milk(CondimentDecorator):

    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description = "milk"

    def cost(self):
        return self.beverage.cost() + 0.25


class Mocha(CondimentDecorator):

    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description = "mocha"

    def cost(self):
        return self.beverage.cost() + 0.99


class Soy(CondimentDecorator):

    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description = "soy"

    def cost(self):
        return self.beverage.cost() + 0.45


class Whip(CondimentDecorator):

    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description = "whip"

    def cost(self):
        return self.beverage.cost() + 0.15


if __name__ == "__main__":
    drink1 = Whip(Mocha(HouseBlend()))
    # 1.10 + 0.99 + 0.15 = 2.24
    print(drink1.cost())
    print(drink1.get_description())

    drink2 = Milk(DarkRoast())
    # 0.75 + 0.25 = 1.0
    print(drink2.cost())
    print(drink2.get_description())

    drink3 = Decaf()
    # = 1.25
    print(drink3.cost())
    print(drink3.get_description())

    drink4 = Whip(Whip(Whip(Espresso())))
    # = 2.10 + 0.15 * 3 = 2.55
    print(drink4.cost())
    print(drink4.get_description())
