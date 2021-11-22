
import random

class Dice:
    
    # Constants    
    FACE = 0
    
    # Static variables
   


    # Constructor initializes the state of new dice
    def __init__(self, cast, face):
        # set the attributes (the state in each Coin object)
        self.cast = 0
        self.face = 0
        

    def cast(self):
        self._cast = random.randint(0,6)
        return self.cast
    
    def face(self):
        index = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six"}
        face = index.get(self.cast)
        print (face)
        return self.face
       
    
