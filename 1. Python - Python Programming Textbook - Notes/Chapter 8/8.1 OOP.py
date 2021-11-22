
# OOP = object orientated programming
# Software objects combine attributes and methods
# objects are created from a definition called a class
# a programmer can create many objects from the same class, like a builder creating houses from a blueprint

# example 

class Critter(object):
    """A virtual pet"""
    def talk(self):
        print("Hi.  I'm an instance of class Critter.")
        
        
crit = Critter()
crit.talk()

# class names typically begin with a capital letter
