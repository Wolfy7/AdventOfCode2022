with open('input') as f:
    rucksacks = f.read().splitlines()

sum = 0
for rucksack in rucksacks:
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    shared_item = list(set(compartment1).intersection(compartment2))
    if shared_item[0].islower():
        sum += (ord(shared_item[0]) - 96)
    else:
        sum += (ord(shared_item[0]) - 38)

print(sum)

sum = 0
for rucksack in range(0, len(rucksacks), 3):
    shared_item = list(set(rucksacks[rucksack]).intersection(rucksacks[rucksack+1], rucksacks[rucksack+2]))
    if shared_item[0].islower():
        sum += (ord(shared_item[0]) - 96)
    else:
        sum += (ord(shared_item[0]) - 38)

print(sum)
