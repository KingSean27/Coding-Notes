# by default all of an objects attributes and methods are public, meaning they can be directly accessed by a client
# to encourage encapsulation you can define an attibute or method as private, meaning that only other methods of the object can interact with them
# two underscores tell python it is a private attribute



class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name            # public attribute
        self.__mood = mood          # private attribute

    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")
        
        def __private_method(self): 
            print("This is a private method.")
            
        def public_method(self):
            print("This is a public method.")
            self.__private_method()
       
crit = Critter(name = "Poochie", mood = "happy")

# print(crit.mood)
# will not work as mood is a private attribute so can't be accessed, even if we use __mood

print(crit._Critter__mood)

# as the private attribute is still named it is actually still possible to access
# private attributes just help ourselves really


