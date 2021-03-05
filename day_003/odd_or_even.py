def input_number():
    number = input("type a number: ")
    if not number.isnumeric():
        print("you should type a number")
        number = input_number()
    return int(number)


def is_even(number: int):
    return number % 2 == 0


number = input_number()
if is_even(number):
    print(f"the number {number} is even")
else:
    print(f"the number {number} is odd")


