# docustrings can be used to explain what a function does, use a triple bracket!
# this time rather than calling a global function we are using the function as part of the definition

def capitalize (word):
    """This function capitalises your word """
    word = word.upper ()
    print (word)


word = str(input("Enter Word: "))
capitalize (word)


# No variables created in a function can be accessed outside the function, this is why the return feature is useful

def check(number):
    if number <= 27:
        return "small"
    else:
        return "big"
    
number = int(input("Enter number: "))
check (number)

if check(number) == "small" :
    print(number, "is smaller than 27")
elif check(number) == "big" :
    print(number, "is bigger than 27")
else :
    print()

# this example is important as it shows the return function, this is used so we can use the data outside the function!

