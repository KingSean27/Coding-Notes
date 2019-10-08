

start = int(input("Enter start year: "))
finish = int(input("Enter end year: "))
line = 1
print()

print("Here is a list of leap years between", start, "and", finish, end=":")
print()
print()

for i in range (start, finish):
    if i % 400 == 0: 
        if line % 10 == 0:
            print(start, end=", \n")
            start += 1
            line += 1
        else:
            print(start, end=", ")
            start +=1
            line +=1 
    elif i % 100 != 0 and i % 4 == 0:
        if line % 10 == 0:
            print(start, end=", \n")
            start += 1
            line += 1
        else:
            print(start, end=", ")
            start +=1
            line +=1 
    else:
        start += 1
    
    


