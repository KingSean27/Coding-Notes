
# dictionaries allow you to organise information in pairs
# you look up a key and get it's value
# example from textbooks
# use {} brackets to define and [] brackets to call values 


geek = {"404": "From the web error message 404, meaning page not found.",
        "Googling": "Searching the Internet for background information on a person.",
        "Keyboard Plaque" : "The collection of debris found in computer keyboards.",
        "Link Rot" : "The process by which web page links become obsolete.",}

print(geek["404"])



# a value can't be used to get a key in a dictionary
# as such it's useful to check whether a value is in the dictionary before searching for it and getting an error

x = "405"

if x in geek:
    print(geek["404"])
else:
    print( x, "No value in dictionary")

# the if x in serves as a useful check
# instead of using this we can use the get function, which will return a default value if nothing is found

print(geek.get("Googling"))
print(geek.get("G0000gling"))

# dictionaries are mutable so can be modified

term = input("What term do you want me to add?: ")
if term not in geek:
    definition = input("\nWhat's the definition?: ")
    geek[term] = definition
    print("\n", term, "has been added.")
else:    print("\nThat term already exists!  Try redefining it.")

print(geek)

# be careful not to overwrite terms in a python dictionary!
# a dictionary can't contain multiple items with the same key


