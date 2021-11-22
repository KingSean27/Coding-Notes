# one way to control access to private attributes is to create a property
# a property allows indirect access to attributes and often has some sort of restriction on





class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name
        
    @property #name getter
    def name(self):
        return self.__name
    
# the property is created with a method I want to provide indirect access to (in this case name)
# now the name property of the critter object can be used to get the value of the provate __name attribute

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else: self.__name = new_name
        print("Name change successful.")
        
    def talk(self):
        print("\nHi, I'm", self.name)
        
# this property provides write access, with some limits to the private attribute __name

crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", end= " ")
print(crit.name)
