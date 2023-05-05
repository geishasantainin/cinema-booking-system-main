from visitorinfo import*
from TicketShow import*
from admin import*


global ch

print("---------------------------------------------------")
print("         Welcome To StarWars Cinema Booking        ")
print("---------------------------------------------------")
print()

def start():
    print("1. Admin Registration :")
    print("2. Admin Login        :")
    print("3. Check Ticket       :")


    print()
    adminObj = Admin()
    ch = int(input("Choose Correct option :"))

    if ch == 1:
        adminObj.adminRegistration()



    if ch == 2:
        
        adminObj.adminLogin()

        print()
        print("1. Book Ticket :")
        print("2. Show Ticket :")
        print()
        ch = int(input("Choose Any One Option :"))
        if ch == 1:
            pd_obj = visitorDataCsv()
            pd_obj.getvisitorInfo()
            pd_obj.saveInfo()
        if ch == 2:
            obj = TicketShow()
            obj.ticketShow()

    if ch == 3:
        obj = TicketShow()
        obj.ticketShow()


start()

    

