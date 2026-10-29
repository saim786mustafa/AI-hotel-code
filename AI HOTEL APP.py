
print("===== SAIM HOTEL =====")

rooms = 100
bookings = []

while True:
    print("1. Show Available Rooms")
    print("2. Book a Room")
    print("3. Show Bookings")
    print("4. Check Out")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Available rooms:", rooms)

    elif choice == "2":
        if rooms > 0:
            name = input("Enter customer name: ")
            nights = int(input("Number of nights: "))
            price = nights * 2000

            bookings.append({
                "name": name,
                "nights": nights,
                "price": price
            })

            rooms -= 1
            print("Room booked successfully!")
            print("Total bill: Rs.", price)
        else:
            print("Sorry, no rooms available.")

    elif choice == "3":
        if not bookings:
            print("No bookings yet.")
        else:
            for booking in bookings:
                print("\nCustomer:", booking["name"])
                print("Nights:", booking["nights"])
                print("Bill: Rs.", booking["price"])

    elif choice == "4":
        name = input("Enter customer name: ")
        for booking in bookings:
            if booking["name"].lower() == name.lower():
                bookings.remove(booking)
                rooms += 1
                print("Check-out successful!")
                break
        else:
            print("Booking not found.")

    elif choice == "5":
        print("Thank you for visiting DAIM HOTEL!")
        break

    else:
        print("Invalid option. Try again.")
