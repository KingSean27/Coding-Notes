# two key loops while and for

#any numerical value has the value true if not 0

money = int(input("How much money do you have? "))

if money:
    print("You have money ")
else:
    print("You have no money ")
    
#note that even negative values return a true, it is only 0 which returns false

count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)
    
#this counter neatly shows how the break and continue functions work
#break causes the loop to end and continue causes it to restart

