#you can't alter a string
#however you can create new strings from old ones

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("A new string has been created:", new_message)

print("\nYour message without vowels is:", new_message)

#variable names in all caps are known as constants and refer to a value that is not meant to change
#use constants in programs where you have the same unchanging value used in multiple places
#the lower function is used to that it is lower case, we can only compare letters of the same case
