"""Contains classes pertaining to acme products.

Robert Davis 2021/09/03"""

from random import randint


class Product:
    """A class used for storing data about products."""

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """Initiates the product class"""

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """Returns how stealable a product is as a string
        based on it's price divided by it's weight."""

        steal = self.price / self.weight

        if steal < .5:
            return 'Not so stealable...'
        elif steal < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """Explodes the product.
        Intensity depends on weight and flammability.
        Returns string."""

        boom = self.flammability * self.weight

        if boom < 10:
            return '...fizzle.'
        elif boom < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    """An inheritance of the Product class based
    completely around the product being a boxing glove.\n
    Adds a method called punch() that just punches people,
    and boxing gloves are 100% less explodable!"""

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        """Initiates the boxing glove"""

        super().__init__(
            name,
            price=price,
            weight=weight,
            flammability=flammability
        )

    def explode(self):
        """Explodes the boxing glove."""

        return '...it\'s a glove.'

    def punch(self):
        """Punches me... wait what!?"""

        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
