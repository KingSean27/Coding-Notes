def check():
    global num
    global pokedex
    global x 
    if num in pokedex:
        print("The pokemon you have selected is:", pokedex.get(num))
        num = str(input("What is your pokemon's number: "))
    elif num == "0" :
        x += 1
    else:
       print("Sorry you don't have that pokemon")
       num = str(input("What is your pokemon's number: "))

       
print("Hello welcome to your pokedex, press 0 to exit")
pokedex = { "4":"Charmander", "15":"Beedrill", "97":"Hypno", "109":"Koffing", "145":"Zapdos", "150":"Mewtwo" }
x = 0


num = str(input("What is your pokemon's number: "))


while  x == 0:
    check ()
    continue
else:
    print("Pokedex closing down")
    
# small test program, written to learn about dictionaries 
    