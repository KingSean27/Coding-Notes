# attritubtes such as names can be set
# self automatically recieves a reference so only name will recieve the name input
# you can access and modify an objects attributes outside of it's class
# by using the __str__() in the class definition we can create a string representation for your objects
# this will create a string representation for your object when it is printed


class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
    def __str__(self):
           rep = "Critter object\n"
           rep += "name: " + self.name + "\n"       
    def talk(self):
        print("Hi.  I'm", self.name, "\n")
        
crit1 = Critter(name ="Poochie")
crit1.talk()
crit2 = Critter("Randolph")
crit2.talk()
print("Printing crit1:")
print(crit1.name)



