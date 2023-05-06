import csv

def print_movie():
    movies = []
    with open("movie_info.csv", 'r+', newline="") as f:
        r = csv.reader(f)
        data = list(r)
        for i in data:
            for j in i:
                movies.append(j)
    count = 0
    for movie in movies:
        count += 1
        print(f"{movie}")
        if count % 3 == 0:
            print("____________________")

def add_movie():
    with open("movie_info.csv", 'a+', newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [input("Enter name: "), input("Enter duration: "), input("Enter date: ")])
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



def print_halls():
    halls = []
    with open("halls.csv", 'r+', newline="") as f:
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



