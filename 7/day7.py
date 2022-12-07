with open('input') as f:
    commands = [command.split() for command in f.read().splitlines()]

directories = {'/': []}
cd = ['/']
for command in commands:

    if command[0] == '$' and command[1] == 'cd':
        if command[2] == "/":
            cd = ['/']
        elif command[2] == "..":
            cd.pop()
        else:
            cd.append(command[2])

    elif command[0] == "dir":
        new_dir = "".join(cd) + command[1]
        directories[new_dir] = []
    elif command[0].isdigit():
        directories["".join(cd)].append(int(command[0]))

total = 0
dir_sizes = []
for directory in directories.items():
    dir_size = 0
    dir_size += sum(directory[1])

    for sub_dir in directories:
        if directory[0] in sub_dir and directory[0] != sub_dir:
            dir_size += sum(directories[sub_dir])

    dir_sizes.append(dir_size)
    if dir_size <= 100000:
        total += dir_size

print(total)

for size in sorted(dir_sizes):
    if 70000000 - (max(dir_sizes) - size) >= 30000000:
        print(size)
        break


