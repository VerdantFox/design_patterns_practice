"""Decorator pattern: Starbuzz coffee example."""
import enum


class Size(str, enum.Enum):
    tall = "TALL"
    grande = "GRANDE"
    venti = "VENTI"


SIZE_CONVERTER = {
    Size.tall: 0,
    Size.grande: 1,
    Size.venti: 2
}


class Beverage:

    def __init__(self, size: Size) -> None:
        self.size = size
        self.description = None

    def get_description(self):
        return self.description

    def set_size(self, size: Size):
        self.size = size

    def get_size(self):
        return self.size

    def cost(self):
        raise NotImplementedError("Implement this...")


class HouseBlend(Beverage):

    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = "House blend coffee"

    def cost(self):
        return 1.10 + 0.10 * SIZE_CONVERTER[self.size]


class DarkRoast(Beverage):

    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = "Dark Roast coffee"

    def cost(self):
        return 0.75 + 0.05 * SIZE_CONVERTER[self.size]


class Espresso(Beverage):

    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = "Espresso coffee"

    def cost(self):
        return 2.10 + 0.20 * SIZE_CONVERTER[self.size]


class Decaf(Beverage):

    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = "Decaf coffee"

    def cost(self):
        return 1.25 + 0.15 * SIZE_CONVERTER[self.size]


class CondimentDecorator(Beverage):

    def __init__(self, beverage) -> None:
        self.beverage = beverage
        self.size = self.beverage.size
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
        return self.beverage.cost() + 0.25 + 0.05 * SIZE_CONVERTER[self.size]


class Mocha(CondimentDecorator):

    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description = "mocha"

    def cost(self):
        return self.beverage.cost() + 0.99 + 0.15 * SIZE_CONVERTER[self.size]


class Soy(CondimentDecorator):

    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description = "soy"

    def cost(self):
        return self.beverage.cost() + 0.45 + 0.10 * SIZE_CONVERTER[self.size]


class Whip(CondimentDecorator):

    def __init__(self, beverage) -> None:
        super().__init__(beverage)
        self.description = "whip"

    def cost(self):
        return self.beverage.cost() + 0.15 + 0.05 * SIZE_CONVERTER[self.size]


if __name__ == "__main__":
    drink1 = Whip(Mocha(HouseBlend(Size.venti)))
    # 1.30 + 1.29 + 0.25 = 2.84
    print(drink1.cost())
    print(drink1.get_description())

    drink2 = Milk(DarkRoast(Size.tall))
    # 0.75 + 0.25 = 1.0
    print(drink2.cost())
    print(drink2.get_description())

    drink3 = Decaf(Size.grande)
    # = 1.40
    print(drink3.cost())
    print(drink3.get_description())

    drink4 = Whip(Whip(Whip(Espresso(Size.grande))))
    # = 2.30 + 0.20 * 3 = 2.90
    print(drink4.cost())
    print(drink4.get_description())
