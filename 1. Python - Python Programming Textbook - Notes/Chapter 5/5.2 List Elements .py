
#shows how lists work and shows the list.append function which can be used to add things to a list 

list = ["Amigo", "Hombre", "Esse", "345"]
print(list)

x = str(input("Please add a word: "))
list.append(x)
y = input("Please add a numer: ")
list.append(y)
z = int(input("Pick a number 0 to 5 to delete: "))
print (list[z], "has been deleted")
del list [z]

print(list)



    
