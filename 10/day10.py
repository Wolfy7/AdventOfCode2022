with open('10/input') as f:
    instructions = [instruction.split() for instruction in f.read().splitlines()]

cycles = 1
register = 1
cycle_interest = [20, 60, 100, 140, 180, 220]
signal_strength = []
current_crt_row = []


def cycle(cycles):
    global current_crt_row
    if (cycles % 40 == register) or (cycles % 40 == register + 1) or (cycles % 40 == register + 2):
        current_crt_row.append("#")
    else:
        current_crt_row.append(".")

    if cycles % 40 == 0:
        print(current_crt_row)
        current_crt_row = []

    if cycles in cycle_interest:
        signal_strength.append(cycles * register)
    return cycles + 1


for instruction in instructions:
    if instruction[0] == "noop":
        cycles = cycle(cycles)
    else:
        for _ in range(2):
            cycles = cycle(cycles)
        register += int(instruction[1])

print(sum(signal_strength))
