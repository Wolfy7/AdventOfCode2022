with open('12/input') as f:
    maze = {(x , y): ord(e)-96 if e.islower() else e for y, line in enumerate(f.readlines()) for x, e in enumerate(line.strip())}


def neighbors(maze, x, y):
    for new in [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
        if new not in maze: continue
        if maze[new] - maze[(x, y)] > 1: continue
        yield new


def find_shortest_path(maze, start, end):
    paths, visited, path_indx = [[start]], {start}, 0

    while path_indx < len(paths):
        actual_path = paths[path_indx]
        last_pos = actual_path[-1]
        for neighbor in neighbors(maze, *last_pos):
            if neighbor in visited: continue
            if neighbor == end: return len(actual_path)
            paths.append(actual_path.copy() + [neighbor])
            visited.add(neighbor)
        path_indx += 1
    return 9999999999

start_positions = []
for pos, value in maze.items():
    if value == 'S':
        start = pos
        maze[start] = 1
        start_positions.append(start)
    if value == 'E':
        end = pos
        maze[end] = 26
    if value == 1:
        start_positions.append(pos)

part1 = find_shortest_path(maze, start, end)
print(part1)

part2 = []
for start_pos in start_positions:
    part2.append(find_shortest_path(maze, start_pos, end))

print(min(part2))