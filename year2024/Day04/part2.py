


with open('Day04/input.txt') as f:
    grid = [x.strip() for x in f.readlines()]

mas_x_count = 0

grid_height = len(grid)
grid_width = len(grid[0])

# loop through each cell in the grid, except the edges
# range(1,x-1) does not check the edges, no need in this part
for i in range(1,grid_height-1):
    for j in range(1,grid_width-1):
        if grid[i][j] == 'A':
            # check for two M and two S on the diagonals
            # and make sure the diagonals don't say MAM and SAS
            a = grid[i-1][j-1]
            b = grid[i+1][j+1]
            c = grid[i-1][j+1]
            d = grid[i+1][j-1]
            if ((a == 'M' and b == 'S') or (a == 'S' and b == 'M')) and ((c == 'M' and d == 'S') or (c == 'S' and d == 'M')):
                mas_x_count += 1


print('Part 2:', mas_x_count)
