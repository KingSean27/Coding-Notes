
temp = int(input("Enter first amount in Celsius: "))
lines = int(input("Enter the number of lines for the table: "))
diff = int(input("Enter a whole number difference between lines in Celsius: "))
fara = temp * 1.8 + 32


print("\tCELSIUS", "\tFARENHEIT")
print("")

while lines != 0:
    print ("\t  ", temp , "\t\t", round(fara,1))
    lines = lines - 1
    temp = temp + diff
    fara = temp * 1.8 + 32
    
