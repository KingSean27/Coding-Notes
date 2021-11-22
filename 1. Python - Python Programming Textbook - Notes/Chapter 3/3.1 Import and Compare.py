
#random module can be used to generate random numbers
import random
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = die1 + die2
print("You rolled a", die1, "and a", die2, "for a total of", total)

#if statements are important, have covered before
#note you can use comparison operators on strings and it will see which one is earlier in dictionary
#list of comparison operators in file

if "apple" > "orange":
    print("Apple")
else:
    print("Orange")

#as we know indentation leads to things being in a block

#if multiple elifs are true only the first one will show

die3 = random.randint(1, 100)

if die3 < 10:
    print ("Die 3 is less than 10")
elif die3 < 40:
    print ("Die 3 is less than 40")
elif die3 < 20:
    print ("Die 3 is less than 20")
else:
    print ("Die 3 is larger than 40")

#we can therefore never get the output less than 20 in this statement, as if it is less than 40 that will be the output before
#it reaches the less than 20 line






