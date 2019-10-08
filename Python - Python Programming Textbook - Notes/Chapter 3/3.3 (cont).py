
#using the enter key enters an empty string
#the not condition just works like the opposite, not username is true when username is false
#so hitting enter makes it true so it loops until you enter something else

username = ""
while not username:
    username = input("Username: ")


