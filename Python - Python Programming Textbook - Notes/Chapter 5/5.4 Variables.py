
# be aware that multiple variables can refer to the same thing in python and by chaging it for one you change it for all
# we can avoid this by splicing the list 

mike = ["khakis", "dress shirt", "jacket"]
honey = mike
honey[2] = "red sweater"
print("When not spliced these two will be the same: ")
print(honey)
print(mike, "\n")
    



mike = ["khakis", "dress shirt", "jacket"]
honey = mike[:]
honey[2] = "red sweater"
print("When spliced we will have a copy of the list, so two different things: ")
print(honey)
print(mike)
    
    
