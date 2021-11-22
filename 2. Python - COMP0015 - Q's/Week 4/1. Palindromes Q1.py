

def print_palindrome():
    initial = str(input("Enter Word: "))
    word = initial.lower()
    reverse = word [::-1]

    if reverse == word:
        print (initial, "is a palindrome")
    else:
        print (initial, "is not a palindrome")
        
print_palindrome()

