with open('input') as f:
    sections = f.read().splitlines()

fully_contains = 0
overlap = 0
for section in sections:
    elf1, elf2 = section.split(',')

    elf1 = set([*range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1)])
    elf2 = set([*range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1)])

    if (elf1.issubset(elf2) or elf2.issubset(elf1)):
        fully_contains += 1

    if len(elf1.intersection(elf2)) > 0:
        overlap += 1

print(fully_contains, overlap)