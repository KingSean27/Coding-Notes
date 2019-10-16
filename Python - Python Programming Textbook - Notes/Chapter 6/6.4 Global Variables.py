
# when we have a value that is not global it is known as a shadow value
# this program shows that only global values will change values outside of a function
# it's generally not a good idea to shadow a global variable inside a function as it can lead to confusion
# as they are really two different values

def globe () : 
    global value
    value = value*10
    print ("Multiplied by 10 this value is", value)
    
def shadow():
    value = 10
    print("Shadow value is", value)


value = int(input("Enter Number: "))

globe()
print ("This changes the global value to", value)
shadow()
print("This does not affect the global value: ", value)


# generally you should try to avoid using global variables as much as you can, however using global constants is
# fine and encouraged

# note this is a terrible way to explain this




