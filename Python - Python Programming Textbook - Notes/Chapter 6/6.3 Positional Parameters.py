# this program is useful in showing different ways you can use positional parameters

def birthday1(name, age):
    """ No default values """
    print("Happy birthday,", name, "!", " I hear you're", age, "today.\n")
    
def birthday2(name = "Jackson", age = 1):
    """ Default values """
    print("Happy birthday,", name, "!", " I hear you're", age, "today.\n")
  

birthday1("Jackson", 1)
birthday1(1, "Jackson")
birthday1(name = "Jackson", age = 10)
birthday1(age = 18, name = "Jackson")

birthday2()
birthday2(name = "Katherine")
birthday2(age = 50)
birthday2(name = "Katherine", age = 55)
birthday2("Katherine", 12)
birthday2(22, "Katherine")

# positional parameters get the arguments in order, unless you specify otherwise



