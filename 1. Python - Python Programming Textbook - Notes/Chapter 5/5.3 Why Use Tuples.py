
# at this point it might seem like lists are superior tuples however there are certain advantages to tuples
# they are faster than lists
# Tuples immutability can be a useful feature
# However most of the time for our smaller programs lists are better

# Nested sequences are when lists or tuples contain further lists or tuples, think Russian dolls
# try to avoid more than one level of nesting otherwise it gets too complicated very quickly

# example of a nested sequence

score = [("Moe", 1000), ("Larry", 1500), ("Curly", 3000)]
print(score[1])
print(score[1][1])


# example of unpacking a sequence   

name, score = ("Shemp", 175)
print(name)
print(score)


    
