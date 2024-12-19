

import numpy as np


with open('Day23/input.txt') as f:
    grid = np.array([[y for y in x.strip()] for x in f.readlines()])

counts = np.zeros(grid.shape)

#print(grid)

start = (0,1)
end = (grid.shape[0]-1,grid.shape[1]-2)
UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
opposite = {UP:DOWN,DOWN:UP,LEFT:RIGHT,RIGHT:LEFT}

queue = [(start,DOWN,0)]

# it looks like junctions always keep you moving forward
# we could count all the paths seperately
finish = 0

while len(queue) != 0:
    tile,dire,count = queue.pop(0)
    #print(tile,dire,count)
    if tile == end:
        finish = max(finish,count)
        continue

    match grid[tile]:
        case '.':
            for dire2 in [UP,DOWN,LEFT,RIGHT]:
                # print(dire,dire2)
                if dire2 != opposite[dire]:
                    # print('not opposite')
                    if grid[tile[0]+dire2[0],tile[1]+dire2[1]] != '#':
                        queue.append(((tile[0]+dire2[0],tile[1]+dire2[1]),dire2,count+1))
        case 'v':
            dire2 = DOWN
            if dire2 != opposite[dire]:
                # print('not opposite')
                if grid[tile[0]+dire2[0],tile[1]+dire2[1]] != '#':
                    queue.append(((tile[0]+dire2[0],tile[1]+dire2[1]),dire2,count+1))
        case '>':
            dire2 = RIGHT
            if dire2 != opposite[dire]:
                # print('not opposite')
                if grid[tile[0]+dire2[0],tile[1]+dire2[1]] != '#':
                    queue.append(((tile[0]+dire2[0],tile[1]+dire2[1]),dire2,count+1))
        case '<':
            dire2 = LEFT
            if dire2 != opposite[dire]:
                # print('not opposite')
                if grid[tile[0]+dire2[0],tile[1]+dire2[1]] != '#':
                    queue.append(((tile[0]+dire2[0],tile[1]+dire2[1]),dire2,count+1))
        case '^':
            dire2 = UP
            if dire2 != opposite[dire]:
                # print('not opposite')
                if grid[tile[0]+dire2[0],tile[1]+dire2[1]] != '#':
                    queue.append(((tile[0]+dire2[0],tile[1]+dire2[1]),dire2,count+1))
        case _:
            raise Exception(grid[tile])
        
print(finish)
                    
    




