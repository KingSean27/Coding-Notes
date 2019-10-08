# pickling means to preserve a piece of data
# more complex pieces of data like lists etc can be stored 
# pickled data must be stored in binary
# the shelve module lets you randomly access pickled objects in a file


import pickle
import shelve


print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Classic"]

f = open("pickles1.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()


# the .dump function loads it into the binary file
# we can unpickle the data using the pickle load function

print("\nUnpickling lists.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
brand = pickle.load(f)
shape = pickle.load(f)

print("Variety list:",variety)
print("Shape list:",shape)
print("Brand list:",brand)
f.close()

# we can see that the data has been taken lifted out of the binary file as a list
# Note that it goes through one item at a time and assigns it to the new variable
# so if we change around order of the new variables it won't be right, like we have done here 
