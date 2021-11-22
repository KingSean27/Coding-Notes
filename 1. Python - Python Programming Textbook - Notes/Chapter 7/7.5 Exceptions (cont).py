# you can make an except clause catch multiple types of error


for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
            print("Something went wrong!")
print ("\n")          
            
 # however most of the time it is more useful to split out the types of error:           

for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except TypeError:
         print("I can only convert a string or a number!")
    except ValueError:
         print("I can only convert a string of digits!")
         
# when an exception occurs you may want the argument in it, which is causing the error
# we can do this by setting the value error as a variable
# else clasues are used to when we don't have an exception 


try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
        print("That was not a number! Or as Python would say...")
        print(e)
else:
    print ("Well done you entered a number")