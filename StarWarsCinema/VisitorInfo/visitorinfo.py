import csv

class visitorRegistration():
    def __init__(self):
        self.visitorName = None
        self.noOfvisitor = None
        self.departureLocation = None
        self.destinationLocation = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.selectseatType = None
        self.seatFare = None
        self.autoInc = 1
        self.countcol= 0
        
    def getvisitorInfo(self):
        self.visitorName     = input("Enter visitor Name          :")
        self.noOfvisitor     = int(input("Enter Number Of visitor :"))

        self.ddmmyyyy = input("Enter Date Like 07-05-1992   :")

        print("1: StarWars Part 1")
        print("2: Mandalorian")
        print("3: The Empire strikes back")
        print("4: Avengers")

        self.dl = int(input("Choose movie: "))
        if self.dl == 1:
            self.departureLocation = "StarWars Part 1"
        elif self.dl == 2:
            self.departureLocation = "Mandalorian"
        elif self.dl == 3:
            self.departureLocation = "The Empire strikes back"
        elif self.dl == 4:
            self.departureLocation = "Avengers"
        else:
            print("Please Enter correct choice  :")

        print("1: 11:11")
        print("2: 13:13")
        print("3: 16:16")
        print("4: 20:00")
        self.dpl = int(input("Choose time  :"))
        if self.dpl == 1:
            self.destinationLocation = "11:11"
        elif self.dpl == 2:
            self.destinationLocation = "13:13"
        elif self.dpl == 3:
            self.destinationLocation = "16:16"
        elif self.dpl == 4:
            self.destinationLocation = "20:00"





        seatNoList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28]
        self.bookingList=[]
        while True:
            self.seatNo = int(input("Choose a Seat Number & Max To Max You Can Book Two Ticket  :"))
            if self.seatNo <=30:

                if self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    del seatNoList[self.seatNo-1]
                else:
                    print("Ticket Already Booked")
                print("Do You Want To Book One More Seat Enter (Yes/No)")
                y = input("")
                if y == "Yes":
                    pass
                else:
                    break

            else:
                print("Don't Choose a Seat Number Which is Not Available")

        print(" 1. VIP-Seat     = 1000₽")
        print(" 2. NON VIP-Seat = 400₽")
        self.seatType = int(input("Select Seat Type  :"))

        if self.seatType == 1:
            self.selectseatType = "VIP-Seat"
            self.seatFare = self.noOfvisitor*1000
        elif self.seatType == 2:
            self.selectseatType = "NON VIP-Seat"
            self.seatFare = self.noOfvisitor*400
           
class visitorDataCsv(visitorRegistration):
    def saveInfo(self):
        try:
            with open("bookingdata1.csv", 'r+', newline="") as f:
                r =  csv.reader(f)
                data = list(r)
                for  i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol +=1
                    print()
                print("Number of Records Are Found In Database :",self.autoInc)    
            
        except:
            print("File has not available")
        finally:     
            with open("bookingdata1.csv", 'a+', newline="") as f:
                w =  csv.writer(f)
                w.writerow([self.autoInc,self.visitorName,self.noOfvisitor,self.departureLocation,self.destinationLocation,self.ddmmyyyy,self.bookingList,self.selectseatType,self.seatFare])
                print("Data Save successfully")
                print()
        

'''pd_obj = visitorDataCsv()
pd_obj.getvisitorInfo()
pd_obj.saveInfo()'''