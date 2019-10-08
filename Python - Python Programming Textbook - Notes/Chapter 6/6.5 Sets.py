
# sets are created by using the set([])
# they are like dictionary keys with no values

def sample():
    global a
    a = set(["Hello", "Bye", "Fly"])
    
sample()
print(type(a))

# we can manipulate the sets like lists 
# sets do not allow duplicates to exist 

cities = set(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")
print(cities)
cities.add("Basel")
print(cities)

