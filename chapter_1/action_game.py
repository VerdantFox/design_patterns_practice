"""Action adventure puzzle

Your task:

Arrange the classes.

Identify one abstract class, one interface, and eight classes.

Draw arrows between classes.

a. Draw this kind of arrow for inheritance (“extends”). Images

b. Draw this kind of arrow for interface (“implements”). Images

c. Draw this kind of arrow for HAS-A. Images

Put the method setWeapon() into the right class.

"""


class WeaponBehavior:
    """Base Weapon behavior class."""

    def use_weapon(self):
        """Use a weapon."""
        raise NotImplementedError("Must implement for each weapon class.")


class KnifeBehavior(WeaponBehavior):
    """KnifeBehavior is a WeaponBehavior"""

    def use_weapon(self):
        """Use knife weapon."""
        print("Stabbing!")


class BowAndArrowBehavior(WeaponBehavior):
    """BowAndArrowBehavior is a WeaponBehavior."""

    def use_weapon(self):
        """Use bow and arrow weapon."""
        print("Shooting!")


class AxeBehavior(WeaponBehavior):
    """AxeBehavior is a WeaponBehavior."""

    def use_weapon(self):
        """Use an axe."""
        print("Chopping!")


class SwordBehavior(WeaponBehavior):
    """SwordBehavior is a WeaponBehavior."""

    def use_weapon(self):
        """Use sword."""
        print("Cutting!")


class Character:
    """Base character class. Has a weapon."""

    def __init__(self) -> None:
        self.weapon_behavior = None

    def set_weapon(self, weapon_behavior: WeaponBehavior):
        """Set the weapon behavior to something new."""
        self.weapon_behavior = weapon_behavior

    def fight(self) -> None:
        """Fight with chosen weapon."""
        self.weapon_behavior.use_weapon()


class Queen(Character):
    """Queen is a Character. Has a weapon."""

    def __init__(self) -> None:
        super().__init__()
        self.weapon_behavior = KnifeBehavior()


class King(Character):
    """King is a Character. Has a weapon."""

    def __init__(self) -> None:
        super().__init__()
        self.weapon_behavior = BowAndArrowBehavior()


class Troll(Character):
    """Troll is a Character. Has a weapon."""

    def __init__(self) -> None:
        super().__init__()
        self.weapon_behavior = AxeBehavior()


class Knight(Character):
    """Knight is a Character. Has a weapon."""

    def __init__(self) -> None:
        super().__init__()
        self.weapon_behavior = SwordBehavior()


class ActionGame:
    def main(self):
        king = King()
        troll = Troll()
        king.fight()
        troll.fight()
        king.set_weapon(SwordBehavior())
        king.fight()


if __name__ == "__main__":
    ActionGame().main()
