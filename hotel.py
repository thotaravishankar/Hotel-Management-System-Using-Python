import uuid
from threading import Timer
from datetime import date
class Hotel:
    def __init__(self):
        self.room={101:{"type":"Single-Bed-room","Price":1000,"Status":"Available"},
                   102:{"type":"Single-Bed-room","Price":1000,"Status":"Available"},
                   201:{"type":"Double-Bed-room","Price":1500,"Status":"Available"},
                   202:{"type":"Double-Bed-room","Price":1500,"Status":"Available"},
                   301:{"type":"Deluxe-Suite-room","Price":2500,"Status":"Available"},
                   302:{"type":"Premium-Suite", "Price": 4000, "Status": "Available"},
                   401:{"type":"Premium-Luxury-Suite", "Price": 6000, "Status": "Available"}
                   }
        self.guest={}
        self.booking={}

    def view_room(self):
        print("===================================================================================================")
        print("                                      Available Rooms")
        print("===================================================================================================")
        for i,j in self.room.items():
            print(f"Room number: {i} | Type: {j["type"]} | Price: {j["Price"]} | Status: {j["Status"]} ")
        print("===================================================================================================")

    def register(self):
        name=input("enter your name:")
        phn=input("enter your phone number:")
        if not name or not phn:
            print("Name and Phone Number are required")
        else:
            gid="G"+uuid.uuid4().hex[:5].upper()
            self.guest[gid]={"name":name,"phn":phn}
            print(f"*********Guest registered successfully with ID: {gid}************")

    def guests_list(self):
        if not self.guest:
            print("No Guests are Registered yet.")
        else:
            print("=================================================================================================")
            print("                                      Guest List")
            print("=================================================================================================")
            for i,j in self.guest.items():
                print(f"Guest ID: {i} | Name: {j["name"]} | Phone: {j["phn"]}")
            print("=================================================================================================")

    def book_room(self):
        id=input("enter your guestid:")
        if id in self.guest.keys():
            select=int(input("select room number:"))
            if select not in self.room:
                print("Selected Room is Invalid")
                return
            if self.room[select]["Status"]=="Occupied" or self.room[select]["Status"]=="Reserved" :
                print("Room is Occupied. Select another room")
            elif self.room[select]["Status"]=="Maintenance":
                print("Room is in under maintennace.")
            else:
                self.room[select]["Status"]="Reserved"
                check_in=date.fromisoformat(input("enter check_in date(yyyy-mm-dd):"))
                check_out=date.fromisoformat(input("enter check_out date(yyyy-mm-dd):"))
                bid = "B"+uuid.uuid4().hex[:5].upper()
                nights=(check_out-check_in).days
                total= nights*self.room[select]["Price"]
                print(f"**********{select} Room booked successfully**********")
                self.booking[bid]={"guest id":id,
                                   "name":self.guest[id]["name"],
                                   "Room":select,
                                   "Room Type":self.room[select]["type"],
                                   "Check-IN":check_in,
                                   "Check-OUT":check_out,
                                   "Price":total,
                                   "Nights":nights}

    def view_booking(self):
        if not self.booking:
            print("No One Booked any Room.")
            return
        print("=================================================================================================================================================================")
        print("                                                         Bookings List")
        print("==================================================================================================================================================================")
        for i,j in self.booking.items():
            print(f"Booking ID: {i} | Guest ID: {j["guest id"]} | name: {j["name"]} | Room: {j["Room"]} | Room Type: {j["Room Type"]} | Check-In: {j["Check-IN"]} | Check-OUT: {j["Check-OUT"]} | Nights: {j["nights"]}")
        print("==================================================================================================================================================================")

    def check_in(self):
        bid=input("enter your booking id:")
        if bid not in self.booking:
            print("Not a valid booking id")
        else:
            self.room[self.booking[bid]["Room"]]["Status"]="Occupied"
            print(f"{self.booking[bid]["guest id"]} successfully checked-in")

    def check_out(self):
        bid=input("enter your booking id:")
        if bid not in self.booking.keys():
            print("Not a valid booking id")
        else:
            self.room[self.booking[bid]["Room"]]["Status"]="Maintenance"
            print("Checked-Out success")
            Timer(120,lambda: self.room[self.booking[bid]["Room"]].update({"Status": "Available"})).start()

    def bill(self):
        bid=input("enter your Booking ID:")
        if bid not in self.booking:
            print("Invalid Booking Id")
            return
        print("===================================================================================================")
        print("                                       Bill Receipt")
        print("===================================================================================================")
        print("Booking ID:",bid)
        print("Guest ID:",self.booking[bid]["guest id"])
        print("Name:",self.booking[bid]["name"])
        print("Room Booked:",self.booking[bid]["Room"])
        print("Room Type:",self.booking[bid]["Room Type"])
        print("Nights:",self.booking[bid]["Nights"])
        print("Total Amount:",self.booking[bid]["Price"])
        print()
        print("**Note: Thanks for choosing our premium hotel. Good Wishes**")
        print("===================================================================================================")
print("==========================================================================================================")
print("                                   |Hotel Management System|")
print("==========================================================================================================")
h=Hotel()
while True:
    print()
    choice=input('''Select option:
    1. View Rooms
    2. Register Guest
    3. Guests List
    4. Book a Room
    5. View Bookings
    6. Check-In
    7. Check-OUT
    8. Generate Bill
    9. Exit\n''')
    if choice=="1":
        h.view_room()
    elif choice=="2":
        h.register()
    elif choice=="3":
        h.guests_list()
    elif choice=="4":
        h.book_room()
    elif choice=="5":
        h.view_booking()
    elif choice=="6":
        h.check_in()
    elif choice=="7":
        h.check_out()
    elif choice=="8":
        h.bill()
    elif choice=="9":
        print("**********Thank you visit again***********")
        break
