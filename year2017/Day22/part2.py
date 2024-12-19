

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

TURN_RIGHT = {UP:RIGHT,RIGHT:DOWN,DOWN:LEFT,LEFT:UP}
TURN_LEFT  = {UP:LEFT,LEFT:DOWN,DOWN:RIGHT,RIGHT:UP}



with open('Day22/input.txt') as f:
    grid = [[2 if c=='#' else 0 for c in line] for line in f]
# zero is clean
# one is weak
# two is infected
# three is flagged

# print(grid)
# exit(0)

# position = (1,1)
position = (12,12)
direction = UP


count = 0

for i in range(10000000):
    #print('at',position,direction)
    match grid[position[0]][position[1]]:
        case 0:
            grid[position[0]][position[1]] = 1
            direction = TURN_LEFT[direction]
        case 1:
            grid[position[0]][position[1]] = 2
            count += 1
        case 2:
            grid[position[0]][position[1]] = 3
            direction = TURN_RIGHT[direction]
        case 3:
            grid[position[0]][position[1]] = 0
            # too lazy to put in a reverse, but not lazy enough to not write this long comment that too longer to type
            direction = TURN_RIGHT[TURN_RIGHT[direction]]

    # move forward
    #print('new dir', direction)
    y = position[0]+direction[0]
    x = position[1]+direction[1]
    #print('new pos', (y,x))
    if y < 0:
        # insert line at 0
        #print('y<0')
        grid.insert(0,[0]*len(grid[0]))
    elif y >= len(grid):
        # append line at 0
        #print('y>len',i)
        grid.append([0]*len(grid[0]))
        position = (y,x)
    elif x < 0:
        #print('x<0')
        # insert false at 0 in each line
        for row in grid:
            row.insert(0,0)
    elif x >= len(grid[0]):
        # append false in each line
        #print('x>len',i)
        for row in grid:
            row.append(0)
        position = (y,x)
    else:
        position = (y,x)
    #if i>=6019 and (i-6019)%57 == 0:
    #    print(i,count)
    
#print(grid)
print(count)
