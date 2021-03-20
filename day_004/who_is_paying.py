import random


def add_name() -> str:
    name = input("Type a name: ")
    return name


persons = random.randint(2, 5)
names = list(add_name() for p in range(persons))
lucky_person = random.randint(0, 4)
print(f'{names[lucky_person]} is going to pay the bill. 🎉')
