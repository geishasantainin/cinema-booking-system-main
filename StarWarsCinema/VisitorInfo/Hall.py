from Movie import*
class Hall:
    def __init__(self):
        self.hall_name = None
        self.amount_of_seats = None


    def print_movies(self, hall_name):
        Movie.print_movie()

class Seat(Hall):
    def __init__(self):
        self.x_coord = None
        self.y_coord = None
        self.booked = False







