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
        print(f"{str.upper(movie)}")
        if count % 3 == 0:
            print("____________________")

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
        print(f"{str.upper(user)}")
        if count % 3 == 0:
            print("____________________")

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
