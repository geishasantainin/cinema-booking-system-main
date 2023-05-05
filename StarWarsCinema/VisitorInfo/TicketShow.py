from visitorinfo import*

class TicketShow:

    def ticketShow(self):
        bln = []
        with open("visitorData.csv",'r+',newline="") as f:
            r =  csv.reader(f)
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
        print("",bln[3],"------------->",bln[4],"            ","        Visitor Id:",bln[0])
        print()
        print(" Visitor Name :", bln[1],"              ","Amount of seats :",bln[2])
        print("______________________________________________________________________________")
        print()
        print(" Date of Booking :",bln[5],"              ","Seat No :",bln[6],"              ")
        print()
        print(" Seat Type :       ",bln[7],"                                                           ")
        print(" Price :       ",bln[8],'₽',"                                                           ")
        print()
        print("------------------------------------------------------------------------------")
                




