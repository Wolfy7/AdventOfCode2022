import math

with open('11/input') as f:
    notes = [note.split("\n") for note in f.read().split("\n\n")]


def solve(part1):
    rounds = 20 if part1 else 10_000
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkeys[monkey]["items"]:
                old = int(item)
                worry_level = eval(monkeys[monkey]["operation"])
                worry_level = worry_level // 3 if part1 else worry_level % magic_divisor
                if worry_level % monkeys[monkey]["test"] == 0:
                    next_monkey = f"Monkey {monkeys[monkey]['true']}:"
                    monkeys[next_monkey]["items"].append(worry_level)
                else:
                    next_monkey = f"Monkey {monkeys[monkey]['false']}:"
                    monkeys[next_monkey]["items"].append(worry_level)

                monkeys[monkey]["inspected_items"] += 1

            monkeys[monkey]["items"] = []

    inspected_items = [item["inspected_items"] for item in monkeys.values()]

    inspected_items = sorted(inspected_items)
    print(inspected_items[-1] * inspected_items[-2])


monkeys = {}
for note in notes:
    monkeys[note[0]] = {
        "items": note[1].split(":")[1].split(","),
        "operation": note[2].split(":")[1].strip().removeprefix("new = "),
        "test": int(note[3].split()[-1]),
        "true": note[4].split()[-1],
        "false": note[5].split()[-1],
        "inspected_items": 0
    }

solve(True)

magic_divisor = math.prod([monkey["test"] for monkey in monkeys.values()])
monkeys = {}
for note in notes:
    monkeys[note[0]] = {
        "items": note[1].split(":")[1].split(","),
        "operation": note[2].split(":")[1].strip().removeprefix("new = "),
        "test": int(note[3].split()[-1]),
        "true": note[4].split()[-1],
        "false": note[5].split()[-1],
        "inspected_items": 0
    }

solve(False)