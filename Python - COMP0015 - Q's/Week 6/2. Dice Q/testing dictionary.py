

import random

geek = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six"}
number = random.randint(0,6)
print(number)

print(geek.keys())
match = geek.get(number)
print(match)