DAYS_PER_YEAR = 365
WEEKS_PER_YEAR = 52
MONTHS_PER_YEAR = 12
YEARS_TO_LIVE = 90


def get_age():
    age = input("type your age: ")
    try:
        age = int(age)
        if age >= 90:
            print("you are already older than 90, try again")
            age = get_age()
    except:
        print("you can only type numbers, try again")
        age = get_age()
    return age


def calculate_days(age: int):
    return (YEARS_TO_LIVE - age) * DAYS_PER_YEAR


def calculate_weeks(age: int):
    return (YEARS_TO_LIVE - age) * WEEKS_PER_YEAR


def calculate_months(age: int):
    return (YEARS_TO_LIVE - age) * MONTHS_PER_YEAR


age = get_age()
print(f'You have {calculate_days(age)} days, weeks {calculate_weeks(age)} and {calculate_months(age)} months left')
