from visitorinfo import*
from admin import*
from account import Account, User


global ch

print("---------------------------------------------------")
print("         Welcome To StarWars Cinema Booking        ")
print("---------------------------------------------------")
print()


def ticket_show():
    pass


def start():
    ending = 0
    while ending != 1:
        print("1. Admin Login        :")
        print("2. User Registration  :")
        print("3. User Login         :")
        print("4. Check Ticket       :")



        print()
        ch = int(input("Choose Correct option :"))

        if ch == 1:
            adminObj = Admin()
            adminObj.adminLogin()

        if ch == 2:
            userObj = User()
            userObj.user_registration()

        if ch == 3:
            user = User()
            user.user_login()

        print("Do you want to quit? 1-Yes 0-No")
        ans = input()
        if ans == 1:
            ending = 1
        if ans == 0:
            pass

start()

    

