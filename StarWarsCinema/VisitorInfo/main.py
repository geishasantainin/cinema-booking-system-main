from visitorinfo import*
from account import Account, User, Admin



global ch

print("---------------------------------------------------")
print("         Welcome To StarWars Cinema Booking        ")
print("---------------------------------------------------")
print()


def ticket_show():
    pass


def start():
    while True:
        print("1. Admin Login        :")
        print("2. User Registration  :")
        print("3. User Login         :")


        print()
        ch = int(input("Choose Correct option :"))

        if ch == 1:
            adminObj = Admin()
            adminObj.admin_login()
            adminObj.admin_choice()

        if ch == 2:
            userObj = User()
            userObj.user_registration()

        if ch == 3:
            user = User()
            user.user_login()

        print("Do you want to quit? 1-Yes 0-No")
        ans = int(input())
        if ans == 1:
            break
        elif ans == 0:
            pass


start()

