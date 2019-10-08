

from dice_module import Dice    

def print_menu():
    print("Type:")
    print("\tr - to roll the dice")
    print("\tq - to quit")
    print()
    
    
def main():
    selection = "a"
    selection = input("Enter selection: " )
    
    while selection != 'q':
        if selection == "r":
            die = Dice ()
            die.cast ()
            die.face ()
            selection = input("Enter a selection: ")        
    
    print("\nBye, Bye!\n")
        
print_menu()


      
if __name__ == "__main__":
    main()
