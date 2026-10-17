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
                   302:{"type":"Premium-Suite-room","Price":4000,"Status":"Available"},
                   401:{"type":"Premium-Luxury-Suite","Price":6000,"Status":"Available"}
                   }
        self.guest={}
        self.booking={}

    def view_room(self):
        print("===================================================================================================")
        print("                                      Available Rooms")
        print("===================================================================================================")
        for i,j in self.room.items():
            print(f"Room number: {i} | Type: {j['type']} | Price: {j['Price']} | Status: {j['Status']} ")
        print("===================================================================================================")

    def register(self):
        name=input("enter your name:")
        phn=input("enter your phone number:")
        if not name or not phn:
            print("Name and Phone Number are required")
        else:
            gid="G"+uuid.uuid4().hex[:5].upper().strip()
            self.guest[gid]={"name":name,"phn":phn}
            print(f"*********Guest registered successfully with ID: {gid}************")

    def guests_list(self):
        if not self.guest:
            print("Guests list Empty")
        else:
            print("=================================================================================================")
            print("                                      Guest List")
            print("=================================================================================================")
            for i,j in self.guest.items():
                print(f"Guest ID: {i} | Name: {j['name']} | Phone: {j['phn']}")
            print("=================================================================================================")

    def book_room(self):
        gid=input("enter your guest id:").strip().upper()
        if gid in self.guest.keys():
            try:
                select=int(input("select room number:"))
            except ValueError:
                print("value should be integer")
                return
            if select not in self.room:
                print("Selected Room is Invalid")
                return
            if self.room[select]["Status"]=="Occupied" or self.room[select]["Status"]=="Reserved" :
                print("Room is Occupied. Select another room")
            else:
                try:
                    check_in=date.fromisoformat(input("enter check_in date(yyyy-mm-dd):"))
                except ValueError:
                    print("Invalid date format")
                    return
                if check_in< date.today():
                    print("Past dates not allowed")
                    return
                try:
                    check_out=date.fromisoformat(input("enter check_out date(yyyy-mm-dd):"))
                except ValueError:
                    print("invalid date format")
                    return
                if check_out<=check_in:
                    print("Check-out must be after check-in.")
                    return
                self.room[select]['Status'] = "Reserved"
                bid = "B"+uuid.uuid4().hex[:5].upper().strip()
                nights=(check_out-check_in).days
                total= nights*self.room[select]['Price']
                print(f"**********{select} Room booked successfully**********")
                self.booking[bid]={"guest id":gid,
                                   "name":self.guest[gid]['name'],
                                   "Room":select,
                                   "Room Type":self.room[select]['type'],
                                   "Check-IN":check_in,
                                   "Check-OUT":check_out,
                                   "Price":total,
                                   "Nights":nights,
                                   "Status":"Reserved"}
        else:
            print("guest id is invalid")

    def view_booking(self):
        if not self.booking:
            print("Booking list Empty")
            return
        print("============================================================================================================================================================================================")
        print("                                                         Bookings List")
        print("============================================================================================================================================================================================")
        for i,j in self.booking.items():
            print(f"Booking ID: {i} | Guest ID: {j['guest id']} | name: {j['name']} | Room: {j['Room']} | Room Type: {j['Room Type']} | Check-In: {j['Check-IN']} | Check-OUT: {j['Check-OUT']} | Nights: {j['Nights']} | Status: {j['Status']}")
        print("============================================================================================================================================================================================")

    def check_in(self):
        bid=input("enter your booking id:").strip().upper()
        if bid not in self.booking:
            print("Not a valid booking id")
            return
        if self.booking[bid]['Status']=="Reserved":
            self.room[self.booking[bid]['Room']]['Status']="Occupied"
            self.booking[bid]["Status"]="Checked-IN"
            print(f"{self.booking[bid]['guest id']} successfully checked-in")
        else:
            print("no reserved bookings")

    def check_out(self):
        bid=input("enter your booking id:").strip().upper()
        if bid not in self.booking.keys():
            print("Not a valid booking id")
            return
        if self.booking[bid]['Status']=="Checked-IN":
            self.room[self.booking[bid]['Room']]['Status']="Maintenance"
            self.booking[bid]["Status"]="Checked-OUT"
            print("Checked-Out success")
            t=Timer(120,lambda: self.room[self.booking[bid]['Room']].update({"Status": "Available"}))
            t.daemon =True
            t.start()
        else:
            print("room is not checked-in")

    def cancel(self):
        bid=input("enter your booking id:").strip().upper()
        if bid not in self.booking:
            print("Invalid booking id")
            return
        if self.booking[bid]["Status"]=="Reserved":
            self.room[self.booking[bid]['Room']]['Status']="Available"
            del self.booking[bid]
            print("Room Cancelled Successfully")
        else:
            print("cancellation cannot be done")

    def bill(self):
        bid=input("enter your Booking ID:").strip().upper()
        if bid not in self.booking:
            print("Invalid Booking Id")
            return
        if self.booking[bid]['Status']=="Checked-OUT":
            self.booking[bid]['Status']="Completed"
            print("===================================================================================================")
            print("                                       Bill Receipt")
            print("===================================================================================================")
            print("Booking ID:",bid)
            print("Guest ID:",self.booking[bid]['guest id'])
            print("Name:",self.booking[bid]['name'])
            print("Room Booked:",self.booking[bid]['Room'])
            print("Room Type:",self.booking[bid]['Room Type'])
            print("Nights:",self.booking[bid]['Nights'])
            print("Total Amount:",self.booking[bid]['Price'])
            print()
            print("**Note: Thanks for choosing our premium hotel. Good Wishes**")
            print("===================================================================================================")
        else:
            print("room is not checked-out")
print("==========================================================================================================")
print("                                   |Hotel Management System|")
print("==========================================================================================================")
h=Hotel()
while True:
    choice=input('''Select option:
    1. View Rooms
    2. Register Guest
    3. Guests List
    4. Book a Room
    5. View Bookings
    6. Check-In
    7. Check-OUT
    8. Cancel Booking
    9. Generate Bill
    10. Exit\n''')
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
        h.cancel()
    elif choice=="9":
        h.bill()
    elif choice=="10":
        print("**********Thank you visit again***********")
        break
    else:
        print("Invalid option")
