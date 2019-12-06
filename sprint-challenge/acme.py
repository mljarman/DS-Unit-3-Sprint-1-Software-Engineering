import random

class Product:
    """
    Implements an organization of Acme Corporation's goods.
    """
    def __init__(self, name, price=10, weight=20, flammability=.5, identifier=random.randint(1000000, 999999)):
        self.name = name 
        self.price = price
        self.weight = weight
        self.flammability= flammability
        self.identifier = identifier

    def stealability(self):
        """
        calculates price divided by weight
        """
        price_by_weight = self.price / self.weight
        if price_by_weight < .5:
            return 'Not so stealable'
        if price_by_weight >= .5 and price_by_weight < 1:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'
    
    def explode(self):
        """
        calculates flammability multiplied by weight.
        """
        flam_times_weight = self.flammability * self.weight
        if flam_times_weight < 10:
            return '...fizzle'
        if flam_times_weight >= 10 and flam_times_weight < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

class BoxingGlove(Product):
    """
    Subclass for particular product -- Boxing Glove
    """
    def __init__(self, name)
        super().__init__(name)
        self.weight = 10

    def explode(self):
        """
        override explode method to fit glove
        """
        return "...it's a glove"
    
    def punch(self):
        """
        method commenting on weight of BoxingGlove
        """
        weight = self.weight
        if weight < 5:
            return 'That tickles'
        if weight >= 5 and weight < 15:
            return 'Hey that hurts!'
        else:
            return 'OUCH!'
