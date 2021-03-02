import os

for x in range(1, 101):
	day = format(x, '03')
	os.mkdir(f'day_{day}')
	print(f'folder {day} created successfully')

print("all folders were created successfully")


