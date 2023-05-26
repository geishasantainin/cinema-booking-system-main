from visitorinfo import*
from account import Account, User, Admin
from functions import hall_create1, hall_create2, booking_seat1, booking_seat2


# hall_create1(5, 10)
# hall_create2(5, 10)

global ch

print("---------------------------------------------------")
print("         Welcome To StarWars Cinema Booking        ")
print("---------------------------------------------------")
print()




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
            print("1. FALCON Hall")
            print("2. STARWARS Hall")

            ch = int(input("Choose Hall :"))
            if ch == 1:
                booking_seat1(int(user.password), user.login)
            elif ch == 2:
                booking_seat2(int(user.password), user.login)


        print("Do you want to quit? 1-Yes 0-No")
        ans = int(input())
        if ans == 1:
            break
        elif ans == 0:
            pass


start()

