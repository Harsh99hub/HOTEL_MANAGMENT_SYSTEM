class hotelfarecal():

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print ("\n\n*****WELCOME TO LEELA PLACE HOTEL*****\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        print() #Next Line
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")

        print() #Next Line
        
        print("Your room no.:",self.rno,"\n")
        
    def roomrent(self):
        print() #Next Line
        print ("We have the following rooms for you:-")

        print (r"1.  type A---->rs 6000 PN\-")

        print (r"2.  type B---->rs 5000 PN\-")

        print (r"3.  type C---->rs 4000 PN\-")

        print (r"4.  type D---->rs 3000 PN\-")

        print() #Next Line

        x=int(input("Enter Your Choice Please->"))

        print() #Next Line

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("You have Sucessfully Confirmed room type A")

            self.s=6000*n

        elif (x==2):

            print ("You have Sucessfully Confirmed room type B")

            self.s=5000*n

        elif (x==3):

            print ("You have Sucessfully Confirmed room type C")

            self.s=4000*n

        elif (x==4):
            print ("You have Sucessfully Confirmed room type D")

            self.s=3000*n

        else:

            print ("please choose a room")
            
        print() #Next Line
        
        print ("Your room rent is =",self.s,"\n")

    def restaurentbill(self):
        print()  #Next Line 
        print("*****RESTAURANT MENU*****")

        print() #Next Line

        print("1.water----->Rs20","2.tea----->Rs10",
              "3.breakfast combo--->Rs90","4.lunch---->Rs110",
              "5.dinner--->Rs150","6.Exit")


        while (1):

            print() #Next Line

            c=int(input("Enter your choice:"))


            if (c==1):
                
                print() #Next Line
                
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d

            elif (c==2):
                print() #Next Line
                d=int(input("Enter the quantity:"))
                self.r=self.r+10*d

            elif (c==3):
                print() #Next Line
                d=int(input("Enter the quantity:"))
                self.r=self.r+90*d

            elif (c==4):
                print() #Next Line
                d=int(input("Enter the quantity:"))
                self.r=self.r+110*d

            elif (c==5):
                print() #Next Line
                d=int(input("Enter the quantity:"))
                self.r=self.r+150*d

            elif (c==6):
                print() #Next Line
                break;
            else:
                print("Invalid option")
        print() #Next line

        print ("Total food Cost=Rs",self.r,"\n")

    def	laundrybill(self):
        print() #Next Line
        print ("******LAUNDRY MENU*******")

        print() #Next Line

        print ("1.Shorts----->Rs3","2.Trousers----->Rs4",
               "3.Shirt--->Rs5","4.Jeans---->Rs6",
               "5.Girlsuit--->Rs8","6.Exit")

        while (1):
            
            print() #Next Line

            e=int(input("Enter your choice:"))

            if (e==1):
                print() #Next Line
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                print() #Next Line
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f

            elif (e==3):
                print() #Next Line
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f

            elif (e==4):
                print() #Next Line
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f

            elif (e==5):
                print() #Next Line
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif (e==6):
                print() #Next Line
                break;
            else:

                print ("Invalid option")

        print() #Next Line
        
        print ("Total Laundary Cost=Rs",self.t,"\n")

    def gamebill(self):
        print() #Next Line
        print ("******GAME MENU*******")

        print()# Next line 
        
        print ("1.Table tennis----->Rs60","2.Bowling----->Rs80",
               "3.Snooker--->Rs70","4.Video games---->Rs90",
               "5.Pool--->Rs50==6","6.Exit")


        while (1):

            print() #Next Line
            
            g=int(input("Enter your choice:"))


            if (g==1):
                print() #Next Line
                h=int(input("No. of hours:"))
                self.p=self.p+60*h

            elif (g==2):
                print() #Next Line
                h=int(input("No. of hours:"))
                self.p=self.p+80*h

            elif (g==3):
                print() #Next Line
                h=int(input("No. of hours:"))
                self.p=self.p+70*h

            elif (g==4):
                print() #Next Line
                h=int(input("No. of hours:"))
                self.p=self.p+90*h

            elif (g==5):
                print() #Next Line
                h=int(input("No. of hours:"))
                self.p=self.p+50*h
            elif (g==6):
                print() #Next Line
                break;

            else:

                print ("Invalid option")


        print() #Next Line
        
        print ("Total Game Bill=Rs",self.p,"\n")

    def display(self):
        print()
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
        print ("Your laundary bill is:",self.t)
        print ("Your Game bill is:",self.p)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total bill is:",self.rt)
        print() #Next Line
        print ("Additional Service Charges is",self.a)
        print() #Next Line
        print ("Your Grandtotal bill is:",self.rt+self.a,"\n")
        print() #Next Line
        self.rno+=1

            

        

        

def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate Room Rent")

        print("3.Calculate Restaurant Bill")

        print("4.Calculate Laundry Bill")

        print("5.Calculate Game Bill")

        print("6.Show Total Cost")

        print("7.EXIT")
        
        print() #Next Line

        b=int(input("\nEnter your choice:"))
        print() #Next Line
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

        if (b==7):

            quit()



main()
