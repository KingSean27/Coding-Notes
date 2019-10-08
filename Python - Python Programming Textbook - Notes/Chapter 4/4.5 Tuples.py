
#tuples are like strings, but unlike strigs they can contain elements of any type
#they can include both strings, numbers, images and sounds
#you create tuples by surrounding something in brackets
#since tuples are another type of sequence, everything discussed with strings previously works for them

inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

print("You have", len(inventory), "items in your possession.")

print(inventory)

for item in inventory:
    print(item, end=" ")

#like strings tuples are immutable