with open('input') as f:
    steps = f.read().splitlines()

#         [J]         [B]     [T]
#         [M] [L]     [Q] [L] [R]
#         [G] [Q]     [W] [S] [B] [L]
# [D]     [D] [T]     [M] [G] [V] [P]
# [T]     [N] [N] [N] [D] [J] [G] [N]
# [W] [H] [H] [S] [C] [N] [R] [W] [D]
# [N] [P] [P] [W] [H] [H] [B] [N] [G]
# [L] [C] [W] [C] [P] [T] [M] [Z] [W]
#  1   2   3   4   5   6   7   8   9
crates = {
    '1' : ['L', 'N', 'W', 'T', 'D'],
    '2' : ['C', 'P', 'H'],
    '3' : ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J'],
    '4' : ['C', 'W', 'S', 'N', 'T', 'Q', 'L'],
    '5' : ['P', 'H', 'C', 'N'],
    '6' : ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B'],
    '7' : ['M', 'B', 'R', 'J', 'G', 'S', 'L'],
    '8' : ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T'],
    '9' : ['W', 'G', 'D', 'N', 'P', 'L'],
}

for step in steps:
    step = step.split(' ')

    for moves in range(int(step[1])):
        crate = crates[step[3]].pop()
        crates[step[5]].append(crate)

message = [stack.pop() for stack in crates.values()]
print("".join(message))

crates = {
    '1' : ['L', 'N', 'W', 'T', 'D'],
    '2' : ['C', 'P', 'H'],
    '3' : ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J'],
    '4' : ['C', 'W', 'S', 'N', 'T', 'Q', 'L'],
    '5' : ['P', 'H', 'C', 'N'],
    '6' : ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B'],
    '7' : ['M', 'B', 'R', 'J', 'G', 'S', 'L'],
    '8' : ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T'],
    '9' : ['W', 'G', 'D', 'N', 'P', 'L'],
}

for step in steps:
    step = step.split(' ')

    move_crates = []
    for moves in range(int(step[1])):
        move_crates.append(crates[step[3]].pop())

    for crate in move_crates[::-1]:
        crates[step[5]].append(crate)

message = [stack.pop() for stack in crates.values()]
print("".join(message))