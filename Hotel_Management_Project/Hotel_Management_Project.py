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
    |    1. Book a rooms                                             |
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
            age = int(input("\tEnter your age: "))
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
                    break
                except ValueError:
                    print("\tPlease enter a valid number of days!")
            while True:
                match room_type:
                    case "s":
                        room = rd.choice(single)
                        if single.get(room) == "available":
                            single[room] = [name, room, duration]
                            break
                    case "d":
                        room = rd.choice(double)
                        if double.get(room) == "available":
                            double[room] = [name, room, duration]
                            break
                    case "S":
                        room = rd.choice(suite)
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
    """TODO"""


def check_availability():
    """TODO"""


def checking_out():
    """TODO"""


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
