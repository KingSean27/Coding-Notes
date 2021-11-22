# We can shelve lists together in a file
# the shelf key acts like a dictionary, importantly the shelf key can only be a string 


import pickle
import shelve

print("\nShelving lists.")
s = shelve.open("pickles2")

s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Classic"]

s.sync()

# the sync method makes sure data is written
# since a shelf acts like a dictionary you can access pickled objects from it by supplying a key

print("\nRetrieving lists from a shelved file:")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])

s.close()

# to store more complex information we should use databases, there are many modules which help with this

