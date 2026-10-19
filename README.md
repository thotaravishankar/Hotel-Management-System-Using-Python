# 🏨 Hotel Management System

A **console-based Hotel Management System built using Python** that simplifies hotel room management, guest registration, room reservations, check-in and check-out operations, booking cancellation, and bill generation.

The project uses Python's object-oriented programming concepts and built-in modules to manage guests, rooms, bookings, reservation dates, and room availability.

## 📌 Project Overview

The Hotel Management System provides a simple menu-driven interface for managing hotel operations. Guests can be registered with a unique Guest ID, rooms can be reserved for specific dates, and the system calculates the total booking amount based on the room price and number of nights.

It also manages the booking lifecycle, from reservation to check-out and bill generation. After check-out, a room is temporarily marked as under maintenance before becoming available again.

## ✨ Features

- **View Rooms:** Display room numbers, room types, prices, and current availability.
- **Guest Registration:** Register guests with their name and a validated 10-digit phone number.
- **Unique Guest ID:** Generate a unique guest identifier using UUID.
- **Guest List:** View all registered guests and their details.
- **Room Booking:** Reserve available rooms using a valid Guest ID.
- **Date Validation:** Validate check-in and check-out dates and prevent past-date reservations.
- **Automatic Bill Calculation:** Calculate the total cost based on the number of nights and room price.
- **Booking Management:** View booking details, including Guest ID, room type, dates, price, and status.
- **Check-In:** Change a reservation's status to Checked-IN and the room status to Occupied.
- **Check-Out:** Update the booking status to Checked-OUT and temporarily mark the room as under Maintenance.
- **Booking Cancellation:** Cancel reservations that have not yet been checked in.
- **Bill Generation:** Generate a bill receipt after check-out and mark the booking as Completed.
- **Input Validation:** Handle invalid room numbers, booking IDs, dates, phone numbers, and numeric inputs.

## 🛏️ Room Categories and Pricing

| Room Number | Room Type | Price per Night |
|---|---|---:|
| 101, 102 | Single-Bed Room | ₹1,000 |
| 201, 202 | Double-Bed Room | ₹1,500 |
| 301 | Deluxe Suite Room | ₹2,500 |
| 302 | Premium Suite Room | ₹4,000 |
| 401 | Premium Luxury Suite | ₹6,000 |

*Prices are defined in the Python program and can be modified as required.*

## 🛠️ Technologies Used

- **Python 3** — Core programming language
- **OOP (Object-Oriented Programming)** — Class, objects, methods, and instance attributes
- **`uuid`** — Generate unique guest and booking identifiers
- **`datetime.date`** — Validate reservation dates and calculate the number of nights
- **`re` (Regular Expressions)** — Validate 10-digit phone numbers
- **`threading.Timer`** — Automatically make a checked-out room available again after a 120-second maintenance period
- **Dictionaries** — Store room, guest, and booking information

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.8 or later
- A code editor such as Visual Studio Code, or a terminal

### Step 1: Clone the Repository

```bash
git clone https://github.com/ravi/hotel-management-system.git
```

### Step 2: Navigate to the Project Directory

```bash
cd hotel-management-system
```

### Step 3: Run the Program

Save the Python code in a file named `hotel.py`, then execute:

```bash
python hotel.py
```

On some Windows systems, you may need to use:

```bash
py hotel.py
```

**Note:** All modules used in this project are part of the Python standard library. No external package installation is required.

## 🚀 How to Use

After running the program, a menu appears with the following options:

```text
==========================================
          Hotel Management System
==========================================

Select option:
1. View Rooms
2. Register Guest
3. Guests List
4. Book a Room
5. View Bookings
6. Check-In
7. Check-OUT
8. Cancel Booking
9. Generate Bill
10. Exit
```

### Booking Workflow

1. Select **View Rooms** to check available rooms and their prices.
2. Select **Register Guest** and enter a name and a valid 10-digit phone number.
3. Save the generated Guest ID.
4. Select **Book a Room** and enter the Guest ID and room number.
5. Enter the check-in and check-out dates in `YYYY-MM-DD` format.
6. The system calculates the number of nights and the total booking amount.
7. Use the generated Booking ID to perform check-in and check-out operations.
8. Generate the bill after successfully checking out.
9. Select **Exit** to close the program.

## 💰 Bill Calculation

The system calculates the total room charge using the following formula:

**Total Amount = Price per Night × Number of Nights**

For example, if a guest books a Double-Bed Room at ₹1,500 per night for 3 nights:

```text
Price per Night : ₹1,500
Number of Nights: 3
Total Amount    : ₹4,500
```

## 📊 Booking Status Lifecycle

A booking progresses through the following statuses:

- `Reserved` — The room has been booked.
- `Checked-IN` — The guest has checked in.
- `Checked-OUT` — The guest has checked out.
- `Completed` — The bill has been generated.
- `Cancelled` — The reservation has been cancelled before check-in.

Room statuses include `Available`, `Reserved`, `Occupied`, and `Maintenance`.

## 📂 Project Structure

```text
hotel-management-system/
│
├── hotel.py
└── README.md
```

## 🎯 Learning Outcomes

This project demonstrates practical Python programming concepts, including:

- Object-oriented programming and class design
- Dictionary-based data management
- Input validation using regular expressions
- Date handling and date arithmetic
- Exception handling with `try` and `except`
- Unique identifier generation
- Conditional statements and loops
- Timer-based task execution
- Implementation of a real-world reservation workflow

## 🔮 Future Enhancements

Potential improvements for future versions include:

- Integrating MySQL or SQLite for persistent data storage
- Preventing overlapping reservations for the same room
- Supporting multiple future reservations per room
- Adding guest search and booking history
- Implementing advance payments and refunds
- Generating downloadable PDF invoices
- Creating a graphical user interface or web application
- Adding administrator login and access control

## 👨‍💻 Author

**Python Hotel Management System Project**

Developed to practice Python, object-oriented programming, date validation, and real-world booking management logic.

## 📄 License

This project is available for educational and learning purposes. Add a specific open-source license if you intend to distribute or reuse the project under defined terms.
