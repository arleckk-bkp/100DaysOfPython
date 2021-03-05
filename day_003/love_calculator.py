name_1 = input('Type your name: ').upper()
name_2 = input('Type your crush name: ').upper()
TRUE = {c: 0 for c in 'TRUE'}
LOVE = {c: 0 for c in 'LOVE'}


for c in TRUE:
    for c1 in name_1:
        if c == c1:
            TRUE[c] = TRUE[c] + 1
    for c2 in name_2:
        if c == c2:
            TRUE[c] = TRUE[c] + 1

for c in LOVE:
    for c1 in name_1:
        if c == c1:
            LOVE[c] = LOVE[c] + 1
    for c2 in name_2:
        if c == c2:
            LOVE[c] = LOVE[c] + 1

true_score = 0
love_score = 0
for key in TRUE:
    true_score += TRUE[key]
for key in LOVE:
    love_score += LOVE[key]

str_score = f"{str(true_score)}{str(love_score)}"
score = int(str_score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")