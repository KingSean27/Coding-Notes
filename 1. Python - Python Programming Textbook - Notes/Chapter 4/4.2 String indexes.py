# the len function outputs the length of a string
# we can check whether values are contained in that string 

length = input("Enter word: ")
print ("The length of your word is: ", len(length))

if "e" in length:
    print("The letter e is in your message")
else:
    print("The letter e is not in your message")
 
    
#when indexing strings we can use their values as a range
#this program picks a random letter in the range of the string 10 times
#note how the negative and positive numbers are opposites

import random
word = input("Please enter word ", )

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])