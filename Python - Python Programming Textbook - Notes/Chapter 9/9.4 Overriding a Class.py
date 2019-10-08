# we've already seen how to extend a class by adding new methods to a derived class
# however we can also redefine how the inherited method of a base class works in a derived class
# you can create a method with completely new functionality or incorporate the functionality of the base class

class Card(object):
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",   "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    """ A Card that won't reveal its
    rank or suit when printed. """
    
    def __str__(self):
        return "<unprintable>"

# this overwrites the string functionality of the card so that it replaces the inherited one
# note that the str functionality of the base class won't be changed 

card1 = Unprintable_Card(rank=2, suit='d')
print(card1)

# next we have a class which takes in the methods of the base class by using the super() method
# this gets the method of the superclass/base class then we can add to it

class Positionable_Card(Card):
    """ A Card that can be face up or face down. """
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up
        
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    
    def flip(self):
        self.is_face_up = not self.is_face_up
        
        
# now we can show how this all works

card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")

print("Printing a Card object:")
print(card1)

print("\nPrinting an Unprintable_Card object:")
print(card2)

print("\nPrinting a Positionable_Card object:")
print(card3)

print("\nFlipping the Positionable_Card object.")
card3.flip()

print("\nPrinting the Positionable_Card object:")
print(card3)

