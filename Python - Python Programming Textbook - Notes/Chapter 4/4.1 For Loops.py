
#the for loop repeats part of a program based on a sequence
#in a string each letter counts as an input

word = input("Enter a word: ")
print("\nHere's each letter in your word:")
for letter in word:
    print(letter)
    
    

#for loops are also very useful when combined with the range function 

print("Counting:")
for i in range(10):
    print(i, end=" ")
    
print("\n\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end=" ")
    
print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end=" ")
