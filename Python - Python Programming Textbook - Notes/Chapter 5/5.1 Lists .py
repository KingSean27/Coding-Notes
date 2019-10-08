
# lists are like tuples but are mutable
# lists work just like tuples so everything you learnt for lists can be used for them
# lists use brackets rather than parenthesis

import time

inventory = ["sword", "armor", "shield", "healing potion"]

print ("Your inventory consists of",end=": ")
for item in inventory:
    print(item, end=", ")

print("\n\nYou are attacked and lose your shield in battle")
time.sleep(2)

del inventory [2]
# remember numbers start at 0

print ("Your inventory consists of",end=": ")
for item in inventory:
    print(item, end=", ")

inventory [0] = "axe"

print ("\n\nYou trade in your sword for an axe:")

print ("Your inventory consists of",end=": ")
for item in inventory:
    print(item, end=", ")


# by setting a number we can then edit items in the list, unlike strings 
# we can use the del function to delete an item from the inventory


    
