VALID_TIPS = ["10", "12", "15"]


def welcome_message():
    print("""
Welcome to the end of the world
░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█
░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█
░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█
░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌
░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█
▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌
█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█
█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█
▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌
▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌
█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█
    """)


def get_bill():
    bill = input("what was the total bill? ")
    if not bill.isnumeric():
        print("wrong input, try again you can only type numeric values")
        bill = get_bill()
    return float(bill)


def get_tip_percentage():
    tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
    if not tip.isnumeric():
        print("wrong input, try again you can only type numeric values")
        tip = get_tip_percentage()
    if tip not in VALID_TIPS:
        print(f"you can only tip {VALID_TIPS}")
        tip = get_tip_percentage()
    return int(tip)


def get_number_of_persons():
    persons = input("How many people would you like to split it? ")
    if not persons.isnumeric():
        print("wrong input, try again you can only type numeric values")
        persons = get_number_of_persons()
    return int(persons)


def calculate_bill_per_person(bill: float, tip_percentage: int, people: int):
    total = (bill + (bill * tip_percentage / 100)) / people
    print(f"Each person must pay: {total}")


welcome_message()
bill = get_bill()
tip = get_tip_percentage()
persons = get_number_of_persons()
calculate_bill_per_person(bill, tip_percentage=tip, people=persons)