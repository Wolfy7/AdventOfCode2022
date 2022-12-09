with open('input') as f:
    grid = [[column for column in row] for row in f.read().splitlines()]

visible_trees = 0
highest_scenic_score = 0
for row_index, row in enumerate(grid):
    if row_index == 0 or row_index == len(grid) -1:
        visible_trees += len(grid)
        continue
    for column_index, column in enumerate(row):
        if column_index == 0 or column_index == len(row) -1:
            visible_trees += 1
            continue

        blocked = False
        sum_trees = 1
        for x, y, l in [(-1 ,0, len(grid)), (1, 0, len(grid)), (0, -1, len(row)), (0, 1, len(row))]:
            trees = 0
            for m in range(1, l):
                visible = True
                cell_x = row_index + (x * m)
                cell_y = column_index + (y * m)

                if (cell_x < 0 or cell_x >= l or cell_y < 0 or cell_y >= l):
                    break

                trees += 1
                if grid[cell_x][cell_y] >= column:
                    visible = False
                    break

            sum_trees *= trees

            if visible:
                blocked = True

        if blocked:
            visible_trees += 1

        if sum_trees > highest_scenic_score:
            highest_scenic_score = sum_trees


print(visible_trees)
print(highest_scenic_score)