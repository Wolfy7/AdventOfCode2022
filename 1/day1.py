with open ('input') as f:
    lines = f.read().splitlines()
    elves = {}
    elf = 0
    food = []
    for data in lines:
        if data == "":
            elves[elf] = food
            elf += 1
            food = []
            continue

        food.append(int(data))

calories = [sum(calories) for calories in elves.values()]

print(max(calories))

print(sum(sorted(calories)[-3:]))
