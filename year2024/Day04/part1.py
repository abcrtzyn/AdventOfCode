


with open('Day04/input.txt') as f:
    grid = [x.strip() for x in f.readlines()]

xmas_count = 0

grid_height = len(grid)
grid_width = len(grid[0])

# check each cell in the grid
for i in range(grid_height):
    for j in range(grid_width):
        # if it is an X, lets check
        if grid[i][j] == 'X':
            # for each direction
            for yoff,xoff in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                # check that the 4 letter string is within the grid
                if 0 <= i+yoff*3 < grid_height and 0 <= j+xoff*3 < grid_width:
                    # see if there is an XMAS in this direction
                    if grid[i+yoff][j+xoff] == 'M' and grid[i+yoff*2][j+xoff*2] == 'A' and grid[i+yoff*3][j+xoff*3] == 'S':
                        xmas_count += 1

print('Part 1:', xmas_count)
