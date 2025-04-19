import datetime
import random

# rooms
single = {
    1: ("None", "available", "001", ""),
    2: ("None", "available", "002", ""),
    3: ("None", "available", "003", ""),
    4: ("None", "available", "004", ""),
    5: ("None", "available", "005", ""),
    6: ("None", "available", "006", ""),
    7: ("None", "available", "007", ""),
    8: ("None", "available", "008", ""),
    9: ("None", "available", "009", ""),
    10: ("None", "available", "010", ""),
}
double = {
    11: ("None", "available", "011", ""),
    12: ("None", "available", "012", ""),
    13: ("None", "available", "013", ""),
    14: ("None", "available", "014", ""),
    15: ("None", "available", "015", ""),
    16: ("None", "available", "016", ""),
    17: ("None", "available", "017", ""),
    18: ("None", "available", "018", ""),
    19: ("None", "available", "019", ""),
    20: ("None", "available", "020", ""),
}
suite = {
    21: ("None", "available", "021", ""),
    22: ("None", "available", "022", ""),
    23: ("None", "available", "023", ""),
    24: ("None", "available", "024", ""),
    25: ("None", "available", "025", ""),
    26: ("None", "available", "026", ""),
    27: ("None", "available", "027", ""),
    28: ("None", "available", "028", ""),
    29: ("None", "available", "029", ""),
    30: ("None", "available", "030", ""),
}
booking_time = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
    10: None,
    11: None,
    12: None,
    13: None,
    14: None,
    15: None,
    16: None,
    17: None,
    18: None,
    19: None,
    20: None,
    21: None,
    22: None,
    23: None,
    24: None,
    25: None,
    26: None,
    27: None,
    28: None,
    29: None,
    30: None,
}

available = {"s": 10, "d": 10, "S": 10}

keywords = {"s": single, "d": double, "S": suite}

keyword = {"s": "single", "d": "double", "S": "suite"}

prices = {"s": 1000, "d": 5000, "S": 10000}


def booking_room():
    global booking_time, single, double, suite, available, keywords
    print("\n---------------Booking----------------")
    name = input("Enter your name: ")
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid integer!")
    if age > 18:
        while True:
            room_type = input(
                "What type of room would you like to book? (Single - 's', Double - 'd', Suite - 'S'): "
            )
            if room_type in ["s", "d", "S"]:
                break
            else:
                print("Please enter a valid room type!")
        while True:
            try:
                duration = int(input("Enter the duration of your stay: "))
                break
            except ValueError:
                print("Please enter a valid number of days!")
        if available[room_type] > 0:
            while True:
                room = random.choice(list(keywords[room_type].keys()))
                if keywords[room_type][room][1] == "available":
                    break
            booking_time[room] = datetime.datetime.now()
            keywords[room_type][room] = (
                name,
                "booked",
                (keywords[room_type][room][2]),
                duration,
            )
            print(
                "Room",
                room,
                "has been booked for you. Your Booking ID (BID) is "
                + str(keywords[room_type][room][2])
                + ", Enjoy your stay!",
            )
            print(f"Duration: {duration} days")
            print(f"Date and Time of booking is: {booking_time[room]}")
            available[room_type] -= 1
            print("\n-----------Enjoy your stay------------")
        else:
            print("Sorry, no rooms are available!")
            print("\n--------------------------------------")
    else:
        print("Sorry, you are too young!")
        print("\n--------------------------------------")


def search():
    global single, double, suite, available, appearance
    print("\n----------------Search----------------")
    while True:
        bid_ = input(
            "\nEnter the booking id to find the room you are looking for(Enter 'IDK' if you don't know the BID): "
        ).lower()
        if bid_ in [
            "001",
            "002",
            "003",
            "004",
            "005",
            "006",
            "007",
            "008",
            "009",
            "010",
            "011",
            "012",
            "013",
            "014",
            "015",
            "016",
            "017",
            "018",
            "019",
            "020",
            "021",
            "022",
            "023",
            "024",
            "025",
            "026",
            "027",
            "028",
            "029",
            "030",
        ]:
            bid_ = int(bid_)
            break
        elif bid_ == "idk":
            break
        else:
            print("Please enter a valid booking ID!")
    name = input("\nEnter the name of the person under which the room was booked: ")
    if bid_ != "idk":
        for a in single:
            if int(single[a][2]) == bid_:
                if single[a][0] == name:
                    appearance = a
                else:
                    appearance = False
        for b in double:
            if int(double[b][2]) == bid_:
                if single[a][0] == name:
                    appearance = b
                else:
                    appearance = False
        for c in suite:
            if int(suite[c][2]) == bid_:
                if single[a][0] == name:
                    appearance = c
                else:
                    appearance = False
        if appearance:
            print(f"The room you're looking for is {appearance}")
            print("\n--------------------------------------")
        else:
            print("Please verify the booking ID and name entered!")
    elif bid_ == "idk":
        print("I am extremely sorry but we can't help you any further!")
        print("\n--------------------------------------")


def check_availability():
    global available
    print("\n--------Availability--------")
    print("\nAvailable Rooms:- ")
    print(
        f"- Single: {available['s']}"
        f"- Double: {available['d']}"
        f"- Suite:  {available['S']}"
    )


def checking_out():
    global booking_time, single, suite, double, keywords, prices, keyword, checkout
    print("\n--------Checking Out--------")
    name = input("\nEnter the name of the person under which the room was booked: ")
    while True:
        room_type = input(
            "What type of room would you like to book? (Single - 's', Double - 'd', Suite - 'S'): "
        )
        if room_type in ["s", "d", "S"]:
            break
        else:
            print("Please enter a valid room type!")
    while True:
        try:
            num = int(input("Enter the number of the room you stayed in: "))
            if num in keywords[room_type]:
                break
            else:
                print("Please enter a valid room number!")
        except ValueError:
            print("Please enter a number!")
    if keywords[room_type][num][1] == "booked":
        if keywords[room_type][num][0] == name:
            checking_out_time = datetime.datetime.now()
            time_spent = int((checking_out_time - booking_time[num]).days)
            if time_spent < keywords[room_type][num][3]:
                print("You are checking out early!")
                choice = input("Do you still want to checkout?(y or n): ")
                if choice.lower() in ["y", "yes", "ye"]:
                    checkout = True
                else:
                    print("\n-----------Enjoy your stay------------")
            elif time_spent == keywords[room_type][num][3]:
                checkout = True
            else:
                print("You've stay for extra days, you will be charged extra!")
                checkout = True
            if checkout:
                print("\n--------------------------------------")
                print("\t     YOUR BILL")
                print(f"Room Number: {num}")
                print(f"Room Type: {(keyword[room_type]).title()}")
                print(f"Customer Name: {name}")
                print(f"Time of Checkout: {checking_out_time}")
                print(f"Total Time spend: {time_spent}")
                print(f"Payment: {time_spent * prices[room_type]}")
                print(f"\n--------------------------------------")
                print(f"\nRoom has been checked out.")
                print(f"THANK YOU FOR STAYING WITH US!")
        else:
            print(
                f"Sorry, {num} is not booked under that name. Please verify the name and room number!"
            )
    else:
        print(f"Room {num} is already available, Please verify the room number!")


while True:
    print("\n_______________________________")
    print("\t     MENU")
    print("\n1. Book a Room")
    print("2. Search for a Room")
    print("3. Check Availability")
    print("4. Checkout")
    print("5. Exit")
    print("\n_______________________________")
    while True:
        try:
            choice = int(input("\nYour Choice: "))
            break
        except ValueError:
            print("Please enter a valid choose!")
    if choice == 1:
        booking_room()
    elif choice == 2:
        search()
    elif choice == 3:
        check_availability()
    elif choice == 4:
        checking_out()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
exit()
