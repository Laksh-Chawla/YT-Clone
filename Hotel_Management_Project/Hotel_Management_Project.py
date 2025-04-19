import random as rd
import datetime as dt

# Room Data
single = {
    1: "available",
    2: "available",
    3: "available",
    4: "available",
    5: "available",
    6: "available",
    7: "available",
    8: "available",
    9: "available",
    10: "available",
}
double = {
    11: "available",
    12: "available",
    13: "available",
    14: "available",
    15: "available",
    16: "available",
    17: "available",
    18: "available",
    19: "available",
    20: "available",
}
suite = {
    21: "available",
    22: "available",
    23: "available",
    24: "available",
    25: "available",
    26: "available",
    27: "available",
    28: "available",
    29: "available",
    30: "available",
}

# Booking Time
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

# Availability
available = {"s": 10, "d": 10, "S": 10}

# Prices
prices = {"s": 1000, "d": 5000, "S": 10000}


def main():
    while True:
        print(
            r"""
    +----------------------------------------------------------------+
    |    Options:                                                    |
    |    1. Book a room                                              |
    |    2. Search for a room                                        |
    |    3. Check Availability                                       |
    |    4. Checkout                                                 |
    |    5. Exit                                                     |
    +----------------------------------------------------------------+
        """,
            end="",
        )
        while True:
            try:
                print(
                    "\n\t+----------------------------------------------------------------+"
                )
                option = int(input("\tYour Choice: "))
                print(
                    "\t+----------------------------------------------------------------+"
                )
                break
            except ValueError:
                print(
                    "\t+----------------------------------------------------------------+"
                )
                print("\n\t\t   Please enter a valid choose!\n", end="")
        match option:
            case 1:
                booking_room()
            case 2:
                search()
            case 3:
                check_availability()
            case 4:
                checking_out()
            case 5:
                break
            case _:
                print("\tInvalid choice. Please try again.")


def booking_room():
    """Books a room"""
    print("\n\t+----------------------------Booking-----------------------------+")
    name = input("\tEnter your name: ").strip().lower()
    while True:
        try:
            age = int(input("\tEnter your age: ").lower().strip())
            break
        except ValueError:
            print("\tPlease enter a valid integer!")
    if age < 18:
        print("\tSorry, you are too young!")
        print("\t+----------------------------------------------------------------+")
    else:
        while True:
            room_type = input(
                "\tWhat type of room would you like to book? (Single - 's', Double - 'd', Suite - 'S'): "
            ).strip()
            if room_type in ["s", "d", "S"]:
                break
            else:
                print("\tPlease enter a valid room type!")
        if available[room_type] > 0:
            while True:
                try:
                    duration = int(input("\tEnter the duration of your stay: "))
                    if duration > 0:
                        break
                except ValueError:
                    print("\tPlease enter a valid number of days!")
            while True:
                match room_type:
                    case "s":
                        room = rd.choice(list(single.keys()))
                        if single.get(room) == "available":
                            single[room] = [name, room, duration]
                            break
                    case "d":
                        room = rd.choice(list(double.keys()))
                        if double.get(room) == "available":
                            double[room] = [name, room, duration]
                            break
                    case "S":
                        room = rd.choice(list(suite.keys()))
                        if suite.get(room) == "available":
                            suite[room] = [name, room, duration]
                            break
            booking_time[room] = dt.datetime.now()
            available[room_type] -= 1
            print(f"Room {room} has been booked for you. Your Booking ID is {room}.")
            print(f"Duration: {duration}")
            print(f"Time of Booking: {(booking_time[room]).strftime('%I:%M %p')}")
            print(f"Date of Booking: {dt.datetime.now().strftime('%d/%m/%Y')}")
            print(
                "\t+----------------------------------------------------------------+"
            )
        else:
            print("\tSorry, no rooms are available!")
            print(
                "\t+----------------------------------------------------------------+"
            )


def search():
    print("\n\t+----------------------------Search------------------------------+")
    while True:
        try:
            bid = (
                input(
                    "\nEnter the booking id to find the room you are looking for(Enter 'IDK' if you don't know the BID): "
                )
                .lower()
                .strip()
            )
            if bid.isnumeric():
                if int(bid) in booking_time:
                    bid = int(bid)
                    break
            elif bid == "idk":
                print("Please return with Booking ID.")
                return
            else:
                print("Please enter a valid Booking ID.")
        except EOFError:
            continue
    name = (
        input("\nEnter the name of the person under which the room was booked: ")
        .lower()
        .strip()
    )
    if bid in single and single[bid][0] == name:
        print(f"The room you're looking for is {bid}.")
    elif bid in double and double[bid][0] == name:
        print(f"The room you're looking for is {bid}.")
    elif bid in suite and suite[bid][0] == name:
        print(f"The room you're looking for is {bid}.")
    else:
        print("Please verify the name under which room was booked!")
    print("\t+----------------------------------------------------------------+")


def check_availability():
    global available
    print("\n\t+-------------------------Availability---------------------------+")
    print("\nAvailable Rooms:- ")
    print(
        f"- Single: {available['s']}"
        f"- Double: {available['d']}"
        f"- Suite:  {available['S']}"
    )
    print("\t+----------------------------------------------------------------+")


def checking_out():
    print("\n\t+--------------------------CheckingOut---------------------------+")
    while True:
        try:
            bid = (
                input(
                    "\nEnter the booking id to find the room you are looking for(Enter 'IDK' if you don't know the BID): "
                )
                .lower()
                .strip()
            )
            if bid.isnumeric():
                if int(bid) in booking_time:
                    bid = int(bid)
                    break
            elif bid == "idk":
                print("Please return with Booking ID.")
                return
            else:
                print("Please enter a valid Booking ID.")
        except EOFError:
            continue
    name = (
        input("\nEnter the name of the person under which the room was booked: ")
        .lower()
        .strip()
    )
    while True:
        room_type = input("Room Type(type 'exit' to escape): ").strip().lower()
        if room_type in ["single", "suite", "double", "exit"]:
            match room_type:
                case "single":
                    if bid in single:
                        _name_ = single[bid][0]
                        price = "s"
                        break
                    else:
                        print("Please enter a room type that matches booking id.")
                case "double":
                    if bid in double:
                        _name_ = double[bid][0]
                        price = "d"
                        break
                    else:
                        print("Please enter a room type that matches booking id.")
                case "suite":
                    if bid in suite:
                        _name_ = suite[bid][0]
                        price = "S"
                        break
                    else:
                        print("Please enter a room type that matches booking id.")
                case "exit":
                    return
        else:
            print("Please enter a valid room type!")
    if name == _name_:
        time_spend = dt.datetime.now() - booking_time[bid]
        print("\n--------------------------------------")
        print("\t     YOUR BILL")
        print(f"Room Number: {bid}")
        print(f"Room Type: {room_type.title()}")
        print(f"Customer Name: {name}")
        print(f"Time of Checkout: {dt.datetime.now().strftime('%I:%M %p')}")
        print(f"Total Time spend: {time_spend}")
        print(f"Payment: {time_spend.days() * prices[price]}")
        print(f"\n--------------------------------------")
        print(f"\nRoom has been checked out.")
        print(f"THANK YOU FOR STAYING WITH US!")
    else:
        print("Name does not match!")
    available[price] += 1
    if price == "s":
        single[bid] = "available"
    elif price == "d":
        double[bid] = "available"
    else:
        suite[bid] = "available"
    booking_time[bid] = None
    print("\t+----------------------------------------------------------------+")


print(
    r"""
+------------------------------------------------------------------------+
|                      _   _       _       _                             |
|                     | | | | ___ | |_ ___| |                            |
|                     | |_| |/ _ \| __/ _ \ |                            |
|                     |  _  | (_) | ||  __/ |                            |
|      __  __         |_| |_|\___/ \__\___|_|                   _        |
|     |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_      |
|     | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|     |
|     | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_      |
|     |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|     |
|                    ____       |___/_           _                       |
|                   |  _ \ _ __ ___ (_) ___  ___| |_                     |
|                   | |_) | '__/ _ \| |/ _ \/ __| __|                    |
|                   |  __/| | | (_) | |  __/ (__| |_                     |
|                   |_|   |_|  \___// |\___|\___|\__|                    |
|                                 |__/                                   |
+------------------------------------------------------------------------+
""",
    end="",
)

main()
