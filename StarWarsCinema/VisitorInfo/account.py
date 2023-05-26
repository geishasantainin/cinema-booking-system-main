from functions import print_movie, print_users, add_movie, delete_movie, delete_user, print_seat1, print_seat2,\
    print_bookings1, print_bookings2
import random
from visitorinfo import*


class Account:

    def __init__(self):
        self.login = None
        self.password = None
        self.id = None


class User(Account):
    def user_registration(self):
        print("Enter your login:")
        self.login = input()
        print("Enter your password(only digitals):")
        self.password = input()
        self.id = random.randrange(1000000, 9999999, 1)
        with open("userdata.csv", 'a+', newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [self.id, self.login, self.password])
            print("Your data have been saved successfully")
            print(f"Your user id is {self.id}")

    def user_login(self):

        with open("userdata.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            flag = 0

        while (flag != 1):
            print("----------------------------------------------------------------")
            print()
            self.login = input("Enter  username  :")
            self.password = input("Enter  password  :")
            for i in range(len(data)):
                if self.login == str(data[i][1]) and self.password == str(data[i][2]):
                    print()
                    print("Login successfully")
                    flag = 1
                    break
            if flag != 1:
                print("Enter correct username and password")
                print()
                print("---------------------------------------------------------------")


class Admin(Account):
    login = "admin"
    password = "admin"

    def admin_login(self):
        actList = []

        with open("adminCredential.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            for i in data:
                for j in i:
                    actList.append(j)

        while (True):
            print("----------------------------------------------------------------")
            print()
            self.login = input("Enter  username  :")
            self.password = input("Enter  password  :")
            if self.login == str(actList[0]) and self.password == str(actList[1]):
                print()
                print("Login successfully")
                break
            else:
                print("Enter correct username and password")
            print()
            print("---------------------------------------------------------------")

    def admin_choice(self):
        print("1. Movies Table       :")
        print("2. User Table         :")
        print("3. Bookings Table     :")

        ch = int(input("Choose Correct option :"))

        if ch == 1:
            print_movie("FALCON")
            print("1. Add Movie       :")
            print("2. Del Movie       :")
            print("3. Exit            :")

            ch_a = int(input("Choose Correct option :"))
            if ch_a == 1:
                add_movie()

            if ch_a == 2:
                delete_movie()

            if ch_a == 3:
                Admin.admin_choice(self)

        elif ch == 2:

            print_users()
            print("1. Del User        :")
            print("2. Exit            :")

            ch_a = int(input("Choose Correct option :"))
            if ch_a == 1:
                delete_user()
            if ch_a == 2:
                Admin.admin_choice(self)

        elif ch == 3:
            print("1. FALCON Hall")
            print("2. STARWARS Hall")

            ch = int(input("Choose Correct option :"))

            if ch == 1:
                print_seat1()
                print_bookings1()
            elif ch == 2:
                print_seat2()
                print_bookings2()





