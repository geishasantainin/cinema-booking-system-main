import csv


def print_movie(hall_name):
    movies = []
    with open("movie_info.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        for i in data:
            movies.append(i)
    count = 0
    for movie in movies:
        if movie[5] == hall_name:
            count = 0
            for i in range(0, 5):
                print(f"{movie[i]}")
                if count == 4:
                    print("____________________")
                count += 1
        else:
            pass

def add_movie():
    with open("movie_info.csv", 'a+', newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [input("Enter name: "), input("Enter duration: "), input("Enter date: "), input("Enter time: "), input("Enter time: "), input("Enter hall name: ")])
        print("Movie added successfully")
    f.close()

def delete_movie():
    mov = input("Enter name of the deleting film: ")
    with open("movie_info.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        movies = []
        for i in range(len(data)):
            if (data[i][0]) != str(mov):
                movies.append(data[i])
    f.close()
    with open("movie_info.csv", 'w+', newline="") as f:
        for i in range(len(movies)):
            w = csv.writer(f)
            w.writerow(
                movies[i])
    f.close()


def print_users():
    users = []
    with open("userdata.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        for i in data:
            for j in i:
                users.append(j)
    count = 0
    for user in users:
        count += 1
        print(f"{user}")
        if count % 3 == 0:
            print("____________________")

def delete_user():
    mov = input("Enter name of the deleting user: ")
    with open("userdata.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        users = []
        for i in range(len(data)):
            if (data[i][1]) != str(mov):
                users.append(data[i])
    f.close()
    with open("userdata.csv", 'w+', newline="") as f:
        for i in range(len(users)):
            w = csv.writer(f)
            w.writerow(
                users[i])
    f.close()


def print_halls1():
    halls = []
    with open("hall1.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        for i in data:
            for j in i:
                halls.append(j)
    count = 0
    for hall in halls:
        count += 1
        print(f"{str.upper(hall)}")
        if count % 3 == 0:
            print("____________________")

def print_halls2():
    halls = []
    with open("hall2.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        for i in data:
            for j in i:
                halls.append(j)
    count = 0
    for hall in halls:
        count += 1
        print(f"{str.upper(hall)}")
        if count % 3 == 0:
            print("____________________")


def hall_create1(rows, columns):
    hall = [0] * rows
    for i in range(rows):
        hall[i] = [0] * columns
    for i in range(rows):
        for j in range (columns):
            with open("hall1.csv", 'a+', newline="") as f:
                w = csv.writer(f)
                w.writerow(
                    [i, j, hall[i][j]])

def hall_create2(rows, columns):
    hall = [0] * rows
    for i in range(rows):
        hall[i] = [0] * columns
    for i in range(rows):
        for j in range (columns):
            with open("hall2.csv", 'a+', newline="") as f:
                w = csv.writer(f)
                w.writerow(
                    [i, j, hall[i][j]])


def print_seat1():
    rows = 5
    columns = 10
    seats = []
    with open("hall1.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        seats = list(r)
        lalala = []
        for i in range(rows * columns):
            if int(seats[i][2]) == 0:
                lalala.append("☖")
            else:
                lalala.append("☗")
        count = 0
        print("  1 2 3 4 5 6 7 8 9 10")
        k= 1
        print(f'{k} ', end='')

        for lala in lalala:

            print(f'{lala} ', end='')
            count += 1
            if count == 10 and k!= 5:
                k+=1
                count = 0
                print("")
                print(f'{k} ',end='')


def print_seat2():
    rows = 5
    columns = 10
    seats = []
    with open("hall2.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        seats = list(r)
        lalala = []
        for i in range(rows * columns):
            if int(seats[i][2]) == 0:
                lalala.append("☖")
            else:
                lalala.append("☗")
        count = 0
        print("  1 2 3 4 5 6 7 8 9 10")
        k= 1
        print(f'{k} ', end='')

        for lala in lalala:

            print(f'{lala} ', end='')
            count += 1
            if count == 10 and k!= 5:
                k+=1
                count = 0
                print("")
                print(f'{k} ',end='')


def booking_seat1(password, login):
    print_movie('FALCON')
    movie = input("Choose yours movie: ")
    time = input("Choose your time: ")
    with open("hall1.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
    f.close()
    print("Choice your seat: ")
    print_seat1()
    print("")
    x = int(input("Enter row number: "))
    y = int(input("Enter column number: "))
    with open("hall1.csv", 'w+', newline="") as f:
        f.close()
    for i in range(0,50):
        if int(data[i][0]) == (x-1) and int(data[i][1]) == (y-1):
            data[i][2] = 1
    for i in range(0, 50):
        with open("hall1.csv", 'a+', newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [data[i][0], data[i][1], data[i][2]])
        f.close()
    with open("userdata.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        users = list(r)
    id = 0
    for user in users:
        if user[1] == login and int(user[2]) == password:
            id = int(user[0])
    with open("bookingdata1.csv", 'a+', newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [id, x, y, time, movie])

def booking_seat2(password, login):
    print_movie('STARWARS')
    movie = input("Choose yours movie: ")
    time = input("Choose your time: ")
    with open("hall2.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
    f.close()
    print("Choice your seat: ")
    print_seat2()
    print("")
    x = int(input("Enter row number: "))
    y = int(input("Enter column number: "))
    with open("hall2.csv", 'w+', newline="") as f:
        f.close()
    for i in range(0,50):
        if int(data[i][0]) == (x-1) and int(data[i][1]) == (y-1):
            data[i][2] = 1
    for i in range(0, 50):
        with open("hall2.csv", 'a+', newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [data[i][0], data[i][1], data[i][2]])
        f.close()
    with open("userdata.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        users = list(r)
    id = 0
    for user in users:
        if user[1] == login and int(user[2]) == password:
            id = int(user[0])
    with open("bookingdata2.csv", 'a+', newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [id, x, y, time, movie])

def print_bookings1():
    bookings = []
    print("")
    with open("bookingdata1.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        for i in data:
            for j in i:
                bookings.append(j)
    count = 0
    print("____________________")
    for book in bookings:

        count += 1
        print(f"{book}")
        if count % 5 == 0:
            print("____________________")

def print_bookings2():
    bookings = []
    print("")
    with open("bookingdata2.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        for i in data:
            for j in i:
                bookings.append(j)
    count = 0
    for book in bookings:
        count += 1
        print(f"{book}")
        if count % 3 == 0:
            print("____________________")

    # def ticket_show(id, login):
    #     with open("bookingdata1.csv", 'r+', newline="") as f:
    #         r = csv.reader(f)
    #         data = list(r)
    #         id = int(input("Enter Your Booking Id  :"))
    #         for i in range(len(data)):
    #             if id == str(data[i][0]):
    #                 print("------------------------------------------------------------------------------")
    #                 print("                              StarWars Cinema                                 ")
    #                 print("------------------------------------------------------------------------------")
    #                 print()
    #                 print(" e_Ticket :", "Address                     : Fontannaya str, 89")
    #                 print("           ", "Phone No\Mob No             : 89990599907,89244219384          ")
    #                 print()
    #                 print("", bln[3], "------------->", bln[4], "            ", "        Visitor Id:", id)
    #                 print()
    #                 print(" Visitor Name :", login, "                                                     ")
    #                 print("______________________________________________________________________________")
    #                 print()
    #                 print()
    #                 print()
    #                 print("------------------------------------------------------------------------------")
def print_bookings_user(user_id):
    bookings = []

    print("")
    with open("bookingdata1.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        for i in data:
            for j in i:
                bookings.append(j)
    count = 0
    print("____________________")
    for book in bookings:
        if book == user_id:
            count += 1
            print(f"{book}")
            if count % 5 == 0:
                print("____________________")



    print("1. FALCON Hall")
    print("2. STARWARS Hall")

    ch = int(input("Choose Hall :"))
    if ch == 1:
        booking_seat1(int(user.password), user.login)
    elif ch == 2:
        booking_seat2(int(user.password), user.login)