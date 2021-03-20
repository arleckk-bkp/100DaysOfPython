row1 = ["◼", "◼", "◼"]
row2 = ["◼", "◼", "◼"]
row3 = ["◼", "◼", "◼"]
treasure_map = [row1, row2, row3]
print(f"   A    B    C\n1{row1}\n2{row2}\n3{row3}")
position = input("Where do you want to put the treasure example (A1)?: ").upper()
row = int(position[1]) - 1
column = ord(position[0]) - 65
treasure_map[row][column] = "❌"

for v in treasure_map:
    print(f"{v}")
