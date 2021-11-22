
#this cheat sheet is used so that you can more easily see how words are sliced
word = "pizza"
print( """   Slicing 'Cheat Sheet'
      0   1   2   3   4   5
      +---+---+---+---+---+
      | p | i | z | z | a |
      +---+---+---+---+---+
      -5  -4  -3  -2  -1 """ )
print("Enter the beginning and ending index for your slice of 'pizza'.")
print("Press the enter key at 'Start' to exit.")

start = None
while start != "":
    start = (input("\nStart: "))
    
    if start:
        start = int(start)
        
        finish = int(input("Finish: "))
        
        print("word[", start, ":", finish, "] is", end=" ")
        print(word[start:finish])
 
 # other examples
print ('Other Examples: ')
print (word[:-1])
print (word[-1:])
# none is pythons way of representing nothing,
# [:] is used for slicing shorthand, note you don't need to fill both sides of the bracket
