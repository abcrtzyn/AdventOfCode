

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

TURN_RIGHT = {UP:RIGHT,RIGHT:DOWN,DOWN:LEFT,LEFT:UP}
TURN_LEFT  = {UP:LEFT,LEFT:DOWN,DOWN:RIGHT,RIGHT:UP}



with open('Day22/input.txt') as f:
    grid = [[c=='#' for c in line] for line in f]


# position = (1,1)
position = (12,12)
direction = UP


count = 0

for _ in range(10000):
    #print('at',position,direction)
    
    if grid[position[0]][position[1]]:
        direction = TURN_RIGHT[direction]
        grid[position[0]][position[1]] = False
    else:
        direction = TURN_LEFT[direction]
        grid[position[0]][position[1]] = True
        count += 1
    # move forward
    #print('new dir', direction)
    y = position[0]+direction[0]
    x = position[1]+direction[1]
    #print('new pos', (y,x))
    if y < 0:
        # insert line at 0
        #print('y<0')
        grid.insert(0,[False]*len(grid[0]))
    elif y >= len(grid):
        # append line at 0
        #print('y>len')
        grid.append([False]*len(grid[0]))
        position = (y,x)
    elif x < 0:
        #print('x<0')
        # insert false at 0 in each line
        for row in grid:
            row.insert(0,False)
        
    elif x >= len(grid[0]):
        #print('x>len')
        # append false in each line
        for row in grid:
            row.append(False)
        position = (y,x)
    else:
        position = (y,x)
    #print('actual new',position)
#print(grid)
print(count)
