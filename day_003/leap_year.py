def is_leap_year(year: int):
    is_leap = False
    if year % 4 == 0:
        is_leap = True
        if year % 100 == 0:
            is_leap = False
            if year % 400 == 0:
                is_leap = True
    return is_leap


year = int(input('Which year do you want to check?: '))
if is_leap_year(year):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")