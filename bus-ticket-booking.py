import random

# Bus details
bus_numbers = [201, 202, 203,204]
from_cities = ["Chennai", "Salem", "Chennai", "Attur"]
to_cities = ["Salem", "Chennai", "Attur", "Chennai"]
total_seats = [5, 10, 7,10]
booked_seats = [0, 0, 0, 0]

# Empty list
bookings = []

# OTP generation 
def generate_otp():
    return random.randrange(1000, 9999)

# show avail buses
def Avail_buses():
    print("\nAvailable Buses:")
    for i in range(len(bus_numbers)):
        available = total_seats[i] - booked_seats[i]
        print(f"Bus No: {bus_numbers[i]}, From: {from_cities[i]} To: {to_cities[i]}, Available Seats: {available}")

# book a seat on bus
def book_seat():
    Avail_buses()
    bus_no = int(input("\nEnter the bus number to book: "))
    name = input("Enter your name: ")
    gender = input("Enter Male/Female: ")

    if bus_no in bus_numbers:
        index = bus_numbers.index(bus_no)
        if booked_seats[index] < total_seats[index]:
            otp = generate_otp()
            print(f"Your OTP for booking is: {otp}")
            user_otp = int(input("Enter the OTP to confirm booking: "))
            
            if user_otp == otp:
                booked_seats[index] += 1
                bookings.append((name, bus_no, gender)) 
                print(f"Booking successful for {name} on Bus No: {bus_no}")
            else:
                print("Incorrect OTP. Booking failed.")
        else:
            print("No seats available on this bus.")
    else:
        print("Invalid bus number.")

# show all bookings
def show_bookings():
    if bookings:
        print("\nCurrent Bookings:")
        for booking in bookings:
            print(f"Passenger: {booking[0]}, Bus No: {booking[1]},Gender: {booking[2]}")
    else:
        print("\nNo bookings yet.")

# cancel booking
def cancel_booking():
    show_bookings()
    name = input("\nEnter your name to cancel booking: ")

    for booking in bookings:
        if booking[0] == name:
            bus_no = booking[1]
            otp = generate_otp()
            print(f"Your OTP for booking is: {otp}")
            user_otp = int(input("Enter the OTP for cancellation: "))
            
            if user_otp == otp:
                bookings.remove(booking)
                index = bus_numbers.index(bus_no)
                booked_seats[index] -= 1
                print(f"Booking canceled for {name}.")
            else:
                print("Incorrect OTP. Cancellation failed.")
            return
    print("No booking found for that name.")

# Main menu
def main_menu():
    while True:
        print("\nBUS_TICKET_BOOKING_APPLICATION_by_♡BR♡")
        print("\n1. Available Buses")
        print("2. Book Seat")
        print("3. Show Bookings")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            Avail_buses()
        elif choice == 2:
            book_seat()
        elif choice == 3:
            show_bookings()
        elif choice == 4:
            cancel_booking()
        elif choice == 5:    
        print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# The Main Function
if __name__ == "__main__":
    main_menu()
