# when python fucks up you get an error message known as an exception
# these can be useful as we can use them to work out what exactly went wrong
# the most basic way to handle exceptions is with a try statement with an except clause
# you can specify it to do certain things for certain errors 
import time 

try:
    num = float(input("Enter a number: "))
except ValueError:
    print ("Value Error")
except:
    print("Something went wrong!")


# if you don't know what an error is called you can try to make one yourself

print("Making a divide by 0 error..." )
time.sleep(2)
e = 10/0