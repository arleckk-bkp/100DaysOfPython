def request_number():
    number = input("type a two digits number: ")
    if len(number) != 2:
        request_number()
    return number


def add_two_digits(number: str):
    result = int(number[0]) + int(number[1])
    print(f"the result of {number[0]} + {number[1]} is {result}")


number = request_number()
add_two_digits(number)
