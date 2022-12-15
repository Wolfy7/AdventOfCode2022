from itertools import pairwise

with open('14/input') as f:
    paths = [[eval(coords) for coords in line.split(" -> ")] for line in f.read().splitlines()]


def create_rock_formations(paths):
    cave = set()
    for path in paths:
        for (x1, y1), (x2, y2) in pairwise(path):
            diff_x, diff_y = x2 - x1, y2 - y1
            steps = max(abs(diff_x), abs(diff_y)) + 1
            dx = 0 if diff_x == 0 else diff_x // abs (diff_x)
            dy = 0 if diff_y == 0 else diff_y // abs (diff_y)

            for m in range(steps):
                cave.add((x1 + dx * m, y1 + dy * m))
    return cave


def sand_simulation(cave, deepest):
    sand, dirs = 0, [(0, 1), (-1, 1), (1, 1)]

    while True:
        x, y = 500, 0
        while True:
            if y >= deepest or (500, 0) in cave: return sand
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in cave: break
            else:
                cave.add((x, y))
                sand += 1
                break
            x, y = nx, ny


cave = create_rock_formations(paths)
deepest = max(pos[1] for pos in cave)
part1 = sand_simulation(cave, deepest)

cave = create_rock_formations(paths)
deepest += 2
for x in range(-1000, 1000): cave.add((x, deepest))
part2 = sand_simulation(cave, deepest)

print(part1, part2)
