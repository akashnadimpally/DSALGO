grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

row = len(grid)
column = len(grid[0])


print(row)
print(column)
count = 0
for i in grid:
    for j in i:
        if j < 0:
            count += 1

print(count)