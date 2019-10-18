def loadpokedex():
    global pokedex
    text_file = open("Pokedex.csv", "r")
    for line in text_file:
        both = line.split(',')
        num = int(both[0])
        pokemon = both[1]
        pokedex[num] = pokemon

def check():
    global pokedex
    global close
    try:
        num = int(input("What is your pokemon's number: "))
        if num in pokedex:
            print("The pokemon you have selected is:", pokedex.get(num))
        elif num == 0:
            close += 1
        elif num > 151:
            print('Kanto Pokedex only goes up to 151. Press 0 to exit or pick another choice')
        else:
           print("Sorry that is not a valid number")
    except (TypeError, ValueError):
        print("That is not a valid integer!")

def main():
    global pokedex
    global close
    close = 0
    pokedex = {}
    loadpokedex()
    print("Hello welcome to your Kanto Pokedex, press 0 to exit")

    while close == 0:
        check()
        continue
    else:
        print("Pokedex closing down")

if __name__ == '__main__': main()

# small test program, written to learn about dictionaries