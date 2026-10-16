# 🏨 Hotel Management System

A console-based **Hotel Management System built using Python** that helps manage hotel rooms, guest registrations, room bookings, check-in and check-out operations, and bill generation. This project demonstrates Object-Oriented Programming (OOP), dictionary-based data management, UUID generation, date handling, and timer-based room status updates.

## 📌 Project Overview

The Hotel Management System is designed to simplify basic hotel operations through a menu-driven command-line interface. It allows users to register guests, manage room reservations, track room availability, calculate booking costs, and generate billing receipts.

The system uses Python's built-in modules and stores guest, room, and booking information in dictionaries during program execution.

## ✨ Features

- **View Rooms:** Display room numbers, room types, prices, and current statuses.
- **Guest Registration:** Register guests with their names and phone numbers.
- **Guest List:** View all registered guests along with their unique guest IDs.
- **Room Booking:** Reserve rooms using guest IDs and check-in/check-out dates.
- **Booking Management:** View booking details, including guest information, room details, duration, and total price.
- **Check-In:** Update the room status to `Occupied`.
- **Check-Out:** Update the room status to `Maintenance` after checkout.
- **Automatic Room Availability:** Automatically change the room status to `Available` after a two-minute maintenance period.
- **Bill Generation:** Generate a receipt containing booking information and the total amount.

## 🛏️ Room Categories

| Room Type | Room Numbers | Price per Night |
|---|---|---:|
| Single-Bed Room | 101, 102 | ₹1,000 |
| Double-Bed Room | 201, 202 | ₹1,500 |
| Deluxe Suite Room | 301 | ₹2,500 |
| Premium Suite | 302 | ₹4,000 |
| Premium Luxury Suite | 401 | ₹6,000 |

*Prices are defined in the program and can be modified as needed.*

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Concepts:** Object-Oriented Programming, Classes, Objects, Dictionaries, Conditional Statements, Loops, and Exception Handling concepts
- **Modules:**
  - `uuid` — Generates unique guest and booking IDs.
  - `threading.Timer` — Schedules automatic room status updates.
  - `datetime.date` — Handles check-in and check-out dates.

## ⚙️ How to Run the Project

### Prerequisites

- Python 3.10 or later recommended.
- A code editor or terminal, such as VS Code or Command Prompt.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/Hotel-Management-System.git
```

**2. Navigate to the project directory**

```bash
cd Hotel-Management-System
```

**3. Run the Python program**

Replace `hotel.py` with your actual Python filename if it is different.

```bash
python hotel.py
```

No external Python packages are required.

## 📋 Application Menu

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
8. Generate Bill
9. Exit
```

Select an option from the menu to perform the corresponding operation.

## 💰 Billing Calculation

The total booking amount is calculated based on the number of nights and the selected room's price per night.

**Formula:**

```text
Total Amount = Number of Nights × Price per Night
```

For example, booking a room costing ₹1,500 per night for three nights results in a total of ₹4,500.

## 🔄 Room Status Workflow

```text
Available
    ↓
Reserved
    ↓
Occupied (Check-In)
    ↓
Maintenance (Check-Out)
    ↓
Available (After 2 Minutes)
```

The two-minute maintenance period is intended for demonstration purposes and can be changed in the code.

## 📂 Project Structure

```text
Hotel-Management-System/
│
├── hotel.py
└── README.md
```

## ⚠️ Current Limitations

- Guest, room, and booking data are stored in memory and are lost when the program terminates.
- The system does not use a database.
- Advanced validation for dates, overlapping reservations, and invalid user inputs can be added.
- Room availability is currently managed using a single status per room rather than date-based availability.
- The two-minute maintenance timer is a demonstration feature, not a production-ready housekeeping workflow.

## 🚀 Future Enhancements

- Integrate MySQL or SQLite for persistent data storage.
- Add date-based reservations and prevent overlapping bookings.
- Validate check-in and check-out dates.
- Add cancellation and booking modification features.
- Improve error handling and input validation.
- Add payment tracking and more detailed invoices.
- Develop a graphical user interface or web application.

## 🎯 Learning Outcomes

This project provides practical experience with Python classes and objects, data structures, unique ID generation, date calculations, conditional logic, and asynchronous timer execution. It also demonstrates how core Python concepts can be combined to build a simple real-world management application.

## 👨‍💻 Author

**Your Name**

GitHub: [Your GitHub Profile](https://github.com/YOUR-USERNAME)

---

⭐ If you find this project useful, consider giving the repository a star!
