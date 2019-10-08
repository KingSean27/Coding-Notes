# every instance method, that every object of class has must have a special parameter self by definition, otherwise you will get an error
# the first piece of code is the constructor method, aso called the initialisation method or init
# init is specially recognised method name, as it is a constructor it will be called by any newly created critter object
# it is useful to have as it sets the default varibales for objects when they are created 



class Critter(object):
    """A virtual pet"""
    def __init__(self):
        print("A new critter has been born!")
    def talk(self):
            print("\nHi.  I'm an instance of class Critter.")
            
            
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()


