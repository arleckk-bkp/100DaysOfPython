def get_height():
    return float(input("type your height: "))


def get_weight():
    return float(input("type your weight: "))


bmi = (get_weight() / get_height() ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi} and you have underweight")
elif bmi < 25:
    print(f"your bmi is {bmi} and you have a normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi} and you are  overweight")
elif bmi < 35:
    print(f"your bmi is {bmi} and you are obese")
else:
    print(f"your bmi is {bmi} and you are clinically obese")