import random
#Login Details Storing List
user_info = []
#Ticket Booking Details Storing List
name = []
age = []
gender = []
ph_no = []
travels_no = []
from_Location = []
pickup_Location = []
to_Location = []
drop_Location = []
booked_seats = []
available_seats = [f"{row}{seat}" for row in 'ABCDE' for seat in range(1, 6)]  # A1, A2, ..., E5
# OTP generation 
def generate_otp():
    return (random.randrange(1000, 9999))
    
#Login
def login():
    print("\nBUS_TICKET_BOOKING_APPLICATION_by_♡BR♡")
    a=input("\nEnter your name: ")
    b=int(input("Enter your mobile number: "))
    user_info.append(a)
    user_info.append(b)
    
    otp=generate_otp()
    print(f"\nYour OTP for loging IN is: {otp}")
    user_otp = int(input("\nEnter the OTP for loging IN : "))
   
    if user_otp == otp:
        print("\nUser loging IN is Successfull" )
    else:
        print("Incorrect OTP. Try again.")
        user_otp = int(input("\nEnter the OTP for loging IN : "))
        if user_otp == otp:
            print("\nUser loging IN is Successfull" )
        else:
            print("Sorry, Try Again Later")
            raise SystemExit 
#UserInfo
        
def my_info():
    print(f"Name = {user_info[0]} \nMobile = {user_info[1]}")
    main_menu()
#Travels Lists
def travels_list():
    print("\nAvailable Travels Lists")
    print("\n1 . Barath_Travels")
    print("2 . Roh_Travels")
    print("3 . BR_Travels")
    print("4 . SG_Holidays")
    print("5 . GBRS_Transports")
    
def display_seats():
    print("\nSeat Layout:")
    print("   1    2    3    4    5")
    for row in 'ABCDE':
        row_seats = [seat if seat not in booked_seats else 'XX' for seat in [f"{row}{seat}" for seat in range(1, 6)]]
        print(f"{row}  {'   '.join(row_seats)}")
    print()  # Blank line for spacing    
    
    
#booking ticket    
def book_ticket():
    print("\nStart to Book Your Tickets")
    count = int(input("\nEnter number of tickets you need to Book : "))
    for i in range(1,count+1):
        print(f"\nEnter pasenger{i} Details")
        a=input("Enter the passenger Name :")
        b=int(input("Enter the passenger Age :"))
        c=input("Enter the passenger Gender:")
        d=int(input("Enter the passenger Ph_no:"))
        name.append(a)
        age.append(b)
        gender.append(c)
        ph_no.append(d)
            
        travels_list()
        choice = int(input("\nSelect your Travels to start your travel: "))

        if choice == 1:
            travels_no.append("Barath_Travels")
        elif choice == 2:
            travels_no.append("Roh_Travels")
        elif choice == 3:
            travels_no.append("BR_Travels")
        elif choice == 4:
            travels_no.append("SG_Holidays")
        elif choice == 5:
            travels_no.append("GBRS_Transports")
    
        else:
            print("Invalid choice. Try again.")
#Selecting from Location    
        print("\nTravel Starting Location")
        print("\n1 . Chennai")
        print("2 . Coimbatore")
        print("3 . Salem")
        print("4 . Attur")
        print("5 . Namakkal")
        choice = int(input("\nSelect your Starting point of the Travel: "))

        if choice == 1:
            from_Location.append("Chennai")
            print("\nPickup Locations_in chennai")
            print("\n1 . Koyambedu")
            print("2 . Aalandur Gate")
            print("3 . Tambaram_Railways station")
            print("4 . Kilambakkam_New Busstand")
            print("5 . Chengalpat")
            choice = int(input("\nSelect your pickup point of the Travel: "))
            if choice == 1:
                pickup_Location.append("Koyambedu")
            elif choice == 2:
                pickup_Location.append("Aalandur Gate")
            elif choice == 3:
                pickup_Location.append("Tambaram_Railways station")
            elif choice == 4:
                pickup_Location.append("Kilambakkam_New Busstand")
            elif choice == 5:
                pickup_Location.append("Chengalpat")
            else:
                print("Invalid choice. Try again.")    
                
                
        elif choice == 2:
            from_Location.append("Coimbatore")
            print("\nPickup Locations_in Coimbatore")
            print("\n1 . Gandhipuram")
            print("2 . Nava india")
            print("3 . Lakshmi Mills")
            print("4 . Hopes")
            print("5 . Airport")
            choice = int(input("\nSelect your pickup point of the Travel: "))
            if choice == 1:
                pickup_Location.append("Gandhipuram")
            elif choice == 2:
                pickup_Location.append("Nava india")
            elif choice == 3:
                pickup_Location.append("Lakshmi Mills")
            elif choice == 4:
                pickup_Location.append("Hopes")
            elif choice == 5:
                pickup_Location.append("Airport")
            else:
                print("Invalid choice. Try again.")
            
        elif choice == 3:
            from_Location.append("Salem")
            print("\nPickup Locations_in Salem")
            print("\n1 . Salem_New_Busstand")
            print("2 . 5_Roads")
            print("3 . Kandhampatti")
            print("4 . Kondalampatti")
            print("5 . Selanaikanpatti")
            choice = int(input("\nSelect your pickup point of the Travel: "))
            if choice == 1:
                pickup_Location.append("Salem_New_Busstand")
            elif choice == 2:
                pickup_Location.append("5_Roads")
            elif choice == 3:
                pickup_Location.append("Kandhampatti")
            elif choice == 4:
                pickup_Location.append("Kondalampatti")
            elif choice == 5:
                pickup_Location.append("Selanaikanpatti")
            else:
                print("Invalid choice. Try again.")
            
        elif choice == 4:
            from_Location.append("Attur")
            print("\nPickup Locations_in Attur")
            print("\n1 . Attur_New_Busstand")
            print("2 . Atr_GH")
            print("3 . Kollampatrai")
            print("4 . Narasingapuram")
            choice = int(input("\nSelect your pickup point of the Travel: "))
            if choice == 1:
                pickup_Location.append("Attur_New_Busstand")
            elif choice == 2:
                pickup_Location.append("Atr_GH")
            elif choice == 3:
                pickup_Location.append("Kollampatrai")
            elif choice == 4:
                pickup_Location.append("Narasingapuram")
            else:
                print("Invalid choice. Try again.")
            
        elif choice == 5:
            from_Location.append("Namakkal")
            print("\nPickup Locations_in Namakkal")
            print("\n1 . Namakkal_New_Busstand")
            print("2 . Namakkal Outer_ByPass")
            print("3 . Trichencode_Pirivu")
            print("4 . Rasipuram")
           
            choice = int(input("\nSelect your pickup point of the Travel: "))
            if choice == 1:
                pickup_Location.append("Namakkal_New_Busstand")
            elif choice == 2:
                pickup_Location.append("Namakkal Outer_ByPass")
            elif choice == 3:
                pickup_Location.append("Trichencode_Pirivu")
            elif choice == 4:
                pickup_Location.append("Rasipuram")
            else:
                print("Invalid choice. Try again.")
                
        else:
            print("Invalid choice. Try again.")        
                
#Selecting To Location      
        print("\nTravel To the Destination")
        print("\n1 . Chennai")
        print("2 . Coimbatore")
        print("3 . Salem")
        print("4 . Attur")
        print("5 . Namakkal")
        choice = int(input("\nSelect your destination of the Travel: "))

        if choice == 1:
            to_Location.append("Chennai")
            print("\nDrop_Locations_in chennai")
            print("\n1 . Koyambedu")
            print("2 . Aalandur Gate")
            print("3 . Tambaram_Railways station")
            print("4 . Kilambakkam_New Busstand")
            print("5 . Chengalpat")
            choice = int(input("\nSelect your Drop_Location of the Travel: "))
            if choice == 1:
                drop_Location.append("Koyambedu")
            elif choice == 2:
                drop_Location.append("Aalandur Gate")
            elif choice == 3:
                drop_Location.append("Tambaram_Railways station")
            elif choice == 4:
                drop_Location.append("Kilambakkam_New Busstand")
            elif choice == 5:
                drop_Location.append("Chengalpat")
            else:
                print("Invalid choice. Try again.")    
        elif choice == 2:
            to_Location.append("Coimbatore")
            print("\nDrop_Locations_in Coimbatore")
            print("\n1 . Gandhipuram")
            print("2 . Nava india")
            print("3 . Lakshmi Mills")
            print("4 . Hopes")
            print("5 . Airport")
            choice = int(input("\nSelect your Drop_Location of the Travel: "))
            if choice == 1:
                drop_Location.append("Gandhipuram")
            elif choice == 2:
                drop_Location.append("Nava india")
            elif choice == 3:
                drop_Location.append("Lakshmi Mills")
            elif choice == 4:
                drop_Location.append("Hopes")
            elif choice == 5:
                drop_Location.append("Airport")
            else:
                print("Invalid choice. Try again.")    
        elif choice == 3:
            to_Location.append("Salem")
            print("\nDrop_Locations_in Salem")
            print("\n1 . Salem_New_Busstand")
            print("2 . 5_Roads")
            print("3 . Kandhampatti")
            print("4 . Kondalampatti")
            print("5 . Selanaikanpatti")
            choice = int(input("\nSelect your Drop_Location of the Travel: "))
            if choice == 1:
                drop_Location.append("Salem_New_Busstand")
            elif choice == 2:
                drop_Location.append("5_Roads")
            elif choice == 3:
                drop_Location.append("Kandhampatti")
            elif choice == 4:
                drop_Location.append("Kondalampatti")
            elif choice == 5:
                drop_Location.append("Selanaikanpatti")
            else:
                print("Invalid choice. Try again.")    
        elif choice == 4:
            to_Location.append("Attur")
            print("\nDrop_Locations_in Attur")
            print("\n1 . Attur_New_Busstand")
            print("2 . Atr_GH")
            print("3 . Kollampatrai")
            print("4 . Narasingapuram")
            choice = int(input("\nSelect your Drop_Location of the Travel: "))
            if choice == 1:
                drop_Location.append("Attur_New_Busstand")
            elif choice == 2:
                drop_Location.append("Atr_GH")
            elif choice == 3:
                drop_Location.append("Kollampatrai")
            elif choice == 4:
                drop_Location.append("Thalaivasal")
            elif choice == 5:
                drop_Location.append("Kallakurichi")
            else:
                print("Invalid choice. Try again.")    
        elif choice == 5:
            to_Location.append("Namakkal")
            print("\nDrop_Locations_in Namakkal")
            print("\n1 . Namakkal_New_Busstand")
            print("2 . Namakkal Outer_ByPass")
            print("3 . Trichencode_Pirivu")
            print("4 . Rasipuram")
            choice = int(input("\nSelect your Drop_Location of the Travel: "))
            if choice == 1:
                drop_Location.append("Namakkal_New_Busstand")
            elif choice == 2:
                drop_Location.append("Rasipuram")
            elif choice == 3:
                drop_Location.append("Namagiripet")
            elif choice == 4:
                drop_Location.append("Thandavarayapuram")
            elif choice == 5:
                drop_Location.append("Attur")
            else:
                print("Invalid choice. Try again.") 
                
        else:
            print("Invalid choice. Try again.")        
#To Select Your Seat                
        print("\nSelect Your Seat Number")   
        
        # Seat Selection
        display_seats()  # Show available seats in grid format

        selected_seat = input("Select your seat (e.g., A1): ").strip().upper()
        if selected_seat in available_seats and selected_seat not in booked_seats:
            booked_seats.append(selected_seat)  # Mark seat as booked
            print(f"Seat {selected_seat} has been booked successfully.")
        else:
            print("Invalid seat choice or seat already booked. Please try again.")
            raise SystemExit

#Confirm Booking                
    otp=generate_otp()
    print(f"\nYour OTP for Booking Confirmation is: {otp}")
    user_otp = int(input("\nEnter the OTP for Confirming Your Booking : "))
   
    if user_otp == otp:
        print("\nYour Ticket Booking is Successfull" )
    else:
        print("Incorrect OTP.Try again")
        user_otp = int(input("\nEnter the OTP for Confirming Your Booking : "))
        if user_otp == otp:
            print("\nYour Ticket Booking is Successfully Completed" )
        else:
            print("Sorry, Try Again Later")
            raise SystemExit 
            
#Show your Bookings            
def show_bookings():
    if len(name) == 0:  # If the name list is empty
        print("\nNo bookings yet.")
    else:
        print("\nYour Booked Tickets:")
        for i in range(len(name)):
            print(f"\nPassenger {i + 1}:")
            print(f"\nPassenger Name: {name[i]} \nAge: {age[i]} \nGender: {gender[i]}\nPhone: {ph_no[i]}\nTravel: {travels_no[i]}\nFrom: {from_Location[i]}\nPickup: {pickup_Location[i]}\nTo: {to_Location[i]}\nDrop: {drop_Location[i]}\nSeat: {booked_seats[i]}")
#To Cancel the Ticket    
def cancel_booking():
    if len(name) == 0:  
        print("\nNo bookings yet.")
    else:
        print("\nYour Booked Tickets:")
        for i in range(len(name)):
            print(f"Passenger {i + 1}: {name[i]}")
        
        choice = int(input("\nEnter the passenger number to cancel their booking: ")) - 1
            
            # Validate the choice
        if choice < 0 or choice >= len(name):
                print("Invalid choice. Please enter a valid passenger number.")
        else:

            # Remove the selected booking
            name.pop(choice)
            age.pop(choice)
            gender.pop(choice)
            ph_no.pop(choice)
            travels_no.pop(choice)
            from_Location.pop(choice)
            pickup_Location.pop(choice)
            to_Location.pop(choice)
            drop_Location.pop(choice)
            booked_seats.pop(choice)

            print("\nBooking canceled successfully.")

        # except ValueError:
        #     print("Invalid input. Please enter a number.")
    
# Main menu
def main_menu():
    while True:
        print("\nBUS_TICKET_BOOKING_APPLICATION_by_♡BR♡")
        print("\n1. User informations")
        print("2. Available Travels")
        print("3. Book Your Tickets")
        print("4. Show your Bookings")
        print("5. Cancel Booking")
        print("6. Exit")

        choice = int(input("\nChoose an option: "))

        if choice == 1:
            my_info()
        elif choice == 2:
            travels_list()
        elif choice == 3:
            book_ticket()
        elif choice == 4:
            show_bookings()
        elif choice == 5:
            cancel_booking()
        elif choice == 6:     
            print("\nThankyou\nGoodbye!")
            break
        else:
            print("Invalid choice. Try again.")
    




login()
main_menu()
