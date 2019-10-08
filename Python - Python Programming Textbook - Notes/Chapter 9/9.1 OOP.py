# in OOP objects interact with each other by sending messages to one another
# they do this by accessig the methods of the other objects
# example program called Death of an Alien to illustrate


class Player(object):
    """ A player in a shooter game. """
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        enemy.die()
        
class Alien(object):
    """ An alien in a shooter game. """
    def die(self):
        print("The alien gasps and says: 'Oh, this is it."
              "This is the big one. \n" 
              "Yes, it's getting dark now. Tell my 1.6 million "
              "larvae that I loved them'")
                          
print("Death of an Alien\n")
hero = Player()
invader = Alien()
hero.blast(invader)

# the alien object recieves the die() method from the players blast 

                         