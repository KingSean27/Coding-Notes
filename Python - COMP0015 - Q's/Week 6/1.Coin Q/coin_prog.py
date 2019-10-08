

from coin_module import Coin     

def print_menu():
    print("Type:")
    print("\tf - to flip the coin")
    print("\tq - to quit")
    print()
    
    
def main():
    selection = "a"
    selection = input("Enter selection: " )
    
    while selection != 'q':
        if selection == "f":
            coinx = Coin ()
            coinx.flip ()
            #or could use
            print(coinx)
            selection = input("Enter a selection: ")        
    
    print("\nBye, Bye!\n")
        
print_menu()


      
if __name__ == "__main__":
    main()
