with open ('input') as f:
    lines = [choose.split(" ") for choose in f.read().splitlines()]

def checkRound(opponent, you):
    if opponent == 'A' and you == 'X' or opponent == 'B' and you == 'Y' or opponent == 'C' and you == 'Z':
        return 3

    if opponent == 'A' and you == 'Z' or opponent == 'B' and you == 'X' or opponent == 'C' and you == 'Y':
        return 0

    return 6

selected_shape = {'X': 1, 'Y': 2, 'Z': 3}

total_score = 0
for round in lines:
    total_score += checkRound(round[0], round[1])
    total_score += selected_shape[round[1]]

print(total_score)


lookup = {'X' : {'A': 'Z', 'B': 'X', 'C': 'Y'}, 'Y' : {'A': 'X', 'B': 'Y', 'C': 'Z'}, 'Z' : {'A': 'Y', 'B': 'Z', 'C': 'X'}}
total_score = 0
for round in lines:
    choose = lookup[round[1]][round[0]]
    total_score += checkRound(round[0], choose)
    total_score += selected_shape[choose]

print(total_score)
