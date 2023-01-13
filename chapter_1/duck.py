"""Strategy pattern simulated ducks."""


class FlyBehavior:
    """Fly behavior interface."""

    def fly(self):
        """Fly that duck."""
        raise NotImplementedError(
            "Implement the fly behavior of a specific duck flight."
        )


class FlyWithWings(FlyBehavior):
    """Fly with wings interface."""

    def fly(self):
        "Fly for real."
        print("I'm flying!")


class FlyNoWay(FlyBehavior):
    """Can't fly interface."""

    def fly(self):
        """Don't fly."""
        print("I can't fly...")


class FlyRocketPowered(FlyBehavior):
    """Fly with rockets."""

    def fly(self):
        """Fly with rockets."""
        print("I'm flying with a rocket!")


class QuackBehavior:
    """Quack behavior interface."""

    def quack(self):
        """Quack behavior interface."""
        raise NotImplementedError(
            "Implement the quack behavior for a specific duck quack"
        )


class Quack(QuackBehavior):
    """Quack behavior interface for a quacking duck."""

    def quack(self):
        """Quack duck, quack!"""
        print("Quack!")


class MuteQuack(QuackBehavior):
    """Quack behavior for ducks that can't quack."""

    def quack(self):
        """Don't quack!"""
        print("<<silence>>")


class Squeak(QuackBehavior):
    """Squeak behavior for ducks that squeak."""

    def quack(self):
        """Squeak!"""
        print("Squeak!")


class Duck:
    """SimDuck"""

    def __init__(self):
        """Init the duck class with the encapsulated methods.

        In the future, these attributes could be set at runtime with this method,
        but for now we'll set them like so.
        """
        self.fly_behavior = None
        self.quack_behavior = None

    def display(self):
        """Display duck. This is different for every duck."""
        raise NotImplementedError("Please override the display method for your duck.")

    def perform_fly(self):
        """Perform a duck fly."""
        self.fly_behavior.fly()

    def perform_quack(self):
        """Perform a duck quack."""
        self.quack_behavior.quack()

    def set_quack_behavior(self, quack_behavior):
        """Set the quack behavior."""
        self.quack_behavior = quack_behavior

    def set_fly_behavior(self, fly_behavior):
        "Set the fly behavior."
        self.fly_behavior = fly_behavior


class MallardDuck(Duck):
    """A mallard duck."""

    def __init__(self):
        """Reimplement the init from duck to provide defaults.

        These could be provided at runtime instead."""
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        """Display the mallard duck."""
        print("I'm a real mallard duck!")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        """Display the model duck"""
        print("I'm a model duck.")


class DuckCall:
    """Duck call that is not a duck but can use a quack"""

    def __init__(self) -> None:
        """Still use composition in case there are different types of quack."""
        self.quack_behavior = Quack()

    def quack(self):
        """Quack calls the quack behavior."""
        self.quack_behavior.quack()


class MiniDuckSimulator:
    """Duck simulator game."""

    def main(self):
        """Run the simulator for the mallard duck."""
        mallard = MallardDuck()
        mallard.display()  # I added this one in...
        mallard.perform_quack()
        mallard.perform_fly()

        model = ModelDuck()
        model.perform_fly()
        model.set_fly_behavior(FlyRocketPowered())
        model.perform_fly()


if __name__ == "__main__":
    MiniDuckSimulator().main()
