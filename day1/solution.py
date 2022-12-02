f = open("inventory.txt", "r")
elfs = f.read().split('\n\n')
calories_arr = []
max_calories=0
for elf in elfs:
    calories = 0
    for item in elf.split('\n'):
        calories += int(item)
    calories_arr.append(calories)
calories_arr.sort()
print(calories_arr[-1], sum(calories_arr[-3:]))