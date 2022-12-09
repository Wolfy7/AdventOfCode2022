with open('9/input') as f:
    motions = [motion.split() for motion in f.read().splitlines()]

directions = {'R': (0, 1), 'U': (-1, 0), 'L': (0, -1), 'D': (1, 0)}

visit_pos = set()
head = [0,0]
tail = [0,0]
visit_pos.add(tuple(tail))
for direction, steps in motions:
    for step in range(int(steps)):
        last_head = head.copy()
        head[0] += directions[direction][0]
        head[1] += directions[direction][1]

        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            tail = last_head
            visit_pos.add(tuple(tail))

print(len(visit_pos))
