from typing import List, Tuple, Dict

# make a grid
import numpy as np

with open('Day21/input.txt') as f:
    grid = np.array([[(y=='#') for y in x.strip()] for x in f.readlines()])

def check_range(y,x):
    return 0 <= y < 131 and 0 <= x < 131

# i will use the fact that from S to the edge is empty
# the shortest taxicab distance to any edge is through that method.

# from the edge of a tile, what is the distance to any cell
# i guess also corners
    
# then, distance from start to any cell = start to edge of tile

# distance from center to any next tile edge
center_to_next_edge = 66

need_distances = [(0,0),(0,65),(0,130),(65,0),(65,65),(65,130),(130,0),(130,65),(130,130)]
dir_to_index: Dict[Tuple[int,int],int] = {(1,1):0,(1,0):1,(1,-1):2,(0,1):3,(0,0):4,(0,-1):5,(-1,1):6,(-1,0):7,(-1,-1):8}


Distances = np.ones((len(need_distances),131,131),np.uint16) * 65535

for l,(y,x) in enumerate(need_distances):
    steps = np.zeros(grid.shape,np.bool8)
    queue: List[Tuple[int,Tuple[int,int]]] = [(0,(y,x))]
    while len(queue) != 0:
        curstep, (cury,curx) = queue.pop(0)
        if steps[cury,curx]:
            continue
        #print(curstep,cury,curx)
        Distances[l,cury,curx] = curstep # this will always be the best
        steps[cury,curx] = True

        if check_range(cury-1,curx) and not grid[cury-1,curx] and not steps[cury-1,curx]:
            #print('adding', cury-1,curx)
            queue.append((curstep+1,(cury-1,curx)))
        if check_range(cury+1,curx) and not grid[cury+1,curx] and not steps[cury+1,curx]:
            #print('adding', cury+1,curx)
            queue.append((curstep+1,(cury+1,curx)))
        if check_range(cury,curx-1) and not grid[cury,curx-1] and not steps[cury,curx-1]:
            #print('adding', cury,curx-1)
            queue.append((curstep+1,(cury,curx-1)))
        if check_range(cury,curx+1) and not grid[cury,curx+1] and not steps[cury,curx+1]:
            #print('adding', cury,curx+1)
            queue.append((curstep+1,(cury,curx+1)))
        

#print(Distances.max()) # 260

# move one tile in every direction, subtract off the proper distance to get to the tile
# if the distance is greater than 260, count all proper cells in the tile
parity_to_max = {False: np.count_nonzero(Distances[dir_to_index[(0,0)]].flatten()[0::2]<=260),
                 True: np.count_nonzero(Distances[dir_to_index[(0,0)]].flatten()[1::2]<=260)}

# if the distance is less than 260, count all proper cells less than distance in the tile



# each time moving out one tile,
# there is the same number of horizontal and vertical tiles
# each will have the same distance and parity
# there is one more of each diagonal tile
# each tile has the same distance and parity

DD = 26501365
total_cells = 0
# iteration -1, parity is odd
# center only
total_cells += parity_to_max[True]
cardinal_distance = DD - 66

# iteration 0, parity is even
# cardinals only
total_cells += 4 * parity_to_max[False]
diagonal_distance = cardinal_distance - 66
cardinal_distance = cardinal_distance - 131

i = 1
while diagonal_distance > 0 or cardinal_distance > 0:
    # count the cardinals
    
    if cardinal_distance >= 260:
        total_cells += 4 * parity_to_max[bool(i%2)]
    elif cardinal_distance < 0:
        pass
    else:
        #print(cardinal_distance)
        # for each cardinal direction add the proper cells
        total_cells += np.count_nonzero(Distances[dir_to_index[(1,0)]].flatten()[(i%2)::2]<=cardinal_distance)
        total_cells += np.count_nonzero(Distances[dir_to_index[(-1,0)]].flatten()[(i%2)::2]<=cardinal_distance)
        total_cells += np.count_nonzero(Distances[dir_to_index[(0,1)]].flatten()[(i%2)::2]<=cardinal_distance)
        total_cells += np.count_nonzero(Distances[dir_to_index[(0,-1)]].flatten()[(i%2)::2]<=cardinal_distance)
        
    cardinal_distance -= 131

    # count the diagonals
    # i is the count of the diagonals
    if diagonal_distance >= 260:
        total_cells += 4*i*parity_to_max[bool(i%2)]
    elif diagonal_distance < 0:
        pass
    else:
        #print(diagonal_distance)
        total_cells += i*np.count_nonzero(Distances[dir_to_index[(1,1)]].flatten()[(i%2)::2]<=diagonal_distance)
        total_cells += i*np.count_nonzero(Distances[dir_to_index[(-1,-1)]].flatten()[(i%2)::2]<=diagonal_distance)
        total_cells += i*np.count_nonzero(Distances[dir_to_index[(-1,1)]].flatten()[(i%2)::2]<=diagonal_distance)
        total_cells += i*np.count_nonzero(Distances[dir_to_index[(1,-1)]].flatten()[(i%2)::2]<=diagonal_distance)

    diagonal_distance -= 131

    i += 1

print(total_cells)

