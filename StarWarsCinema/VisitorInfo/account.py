from visitorinfo import*
from functions import print_movie, print_users


class Account:
    user_num = 1

    def __init__(self):
        self.login = None
        self.password = None


class User(Account):
    def user_registration(self):
        print("Enter your login:")
        self.login = input()
        print("Enter your password:")
        self.password = input()
        with open("userdata.csv", 'a+', newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [Account.user_num, self.login, self.password])
            print("Your data have been saved successfully")
            print(f"Your user number is {self.user_num}")
        Account.user_num += 1

    def user_login(self):
        actList = ["lalala"]

        with open("userdata.csv", 'r+', newline="") as f:
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
            self.user_num = int(input("Enter your user number:"))
            if self.login == str(actList[(self.user_num*3)-1]) and self.password == str(actList[self.user_num*3]):
                print()
                print("Login successfully")
                break
            else:
                print("Enter correct username and password")
            print()
            print("---------------------------------------------------------------")

    def ticket_show(self):
        bln = []
        with open("visitorData.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            id = int(input("Enter Your Booking Id  :"))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break
        print("------------------------------------------------------------------------------")
        print("                              StarWars Cinema                                 ")
        print("------------------------------------------------------------------------------")
        print()
        print(" e_Ticket :", "Address              : Fontannaya str, 89")
        print("           ", "Phone No\Mob No             : 89990599907,89244219384            ")
        print()
        print("", bln[3], "------------->", bln[4], "            ", "        Visitor Id:", bln[0])
        print()
        print(" Visitor Name :", bln[1], "              ", "Amount of seats :", bln[2])
        print("______________________________________________________________________________")
        print()
        print(" Date of Booking :", bln[5], "              ", "Seat No :", bln[6], "              ")
        print()
        print(" Seat Type :       ", bln[7], "                                                           ")
        print(" Price :       ", bln[8], '₽', "                                                           ")
        print()
        print("------------------------------------------------------------------------------")


class Admin(Account, Movie):
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
        print("3. Halls Table        :")
        print("4. Bookings Table     :")

        ch = int(input("Choose Correct option :"))

        if ch == 1:
            print_movie()

        elif ch == 2:

            print_users()

        elif ch == 3:

            print_halls()

        elif ch == 4:

            print_bookings()
