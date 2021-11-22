# class attributes are associated with the class itself not the individual components
# static methods are associated with a class


class Critter(object):
    """A virtual pet"""
    total = 0
    
    @staticmethod
    def status():
        print("\nThe total number of critters is", Critter.total)
        
    def __init__(self, name):
            print("A critter has been born!")
            self.name = name
            Critter.total += 1

print("Accessing the class attribute \nCritter.total:", end=" ")
print(Critter.total)
print("\nCreating critters.")
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")
Critter.status()

# total = 0 is a class definition, it will only be read once when python first sees the class definition
# to access a class attribute use . notation
# static methods are designed to be invoked through a class, not an object
# @staticmethod is an example of a decorator
# since static methods are invoked through a class, no objects of the class need to exist before you can invoke them

