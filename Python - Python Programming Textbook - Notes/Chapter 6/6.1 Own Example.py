
def main ():
    global word
    word = word.lower ()
    print (word)


word = str(input("Enter Word: "))
print(word.capitalize())


if __name__ == '__main__':
    main()


#remeber this problem and how you couldn't make it work originally you had no global before word
# as such the RHS was being called as a local variable, as there was no word defined locally were getting an error
