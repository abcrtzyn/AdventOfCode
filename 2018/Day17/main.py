import numpy as np


grid = np.loadtxt('Day17/grid.txt',np.uint8)


# okay now to simulate some water flow
# standing water acts like clay, that flowing water can not go past it
# so lets fall as flowing water
# if we hit a standing water or clay, flow sideways
# if we fall and hit flowing water, stop, it will flow to the same place


search = []

# find the 2 in the top row
start_x = np.where(grid[0] == 2)[0][0]

current_y = 1
current_x = start_x

def spread(y,x,off):
    search_x = x
    while True:
        search_x += off
        c1 = grid[y,search_x]
        if c1 == 0 or c1 == 3:
            grid[y,search_x] = 3
            c2 = grid[y+1,search_x]
            if c2 == 0:
                # falling from here.
                search.append((y,search_x))
                return True
                
            elif c2 == 1 or c2 == 5:
                # keep flowing
                pass
            else:
                np.savetxt('Day17/gridtest.txt',grid,'%u',' ')
                print('under unknown',c2)
                exit(1)
            
        elif c1 == 1: #clay
            return False

        else:
            np.savetxt('Day17/gridtest.txt',grid,'%u',' ')
            print('spread wall',c1)
            exit(0)

def fill(y,x,off):
    # convert all in a layer to standing water
    search_x = x
    while True:
        search_x += off
        c1 = grid[y,search_x]
        if c1 == 3:
            grid[y,search_x] = 5
        elif c1 == 1: #clay
            return
        else:
            np.savetxt('Day17/gridtest.txt',grid,'%u',' ')
            print('fill bad',c1)
            exit(1)


def get_next():
    if search:
        y, x = search.pop()
        # check that this coordinate is still flowing
        if grid[y,x] == 3:
            return (y,x)
        else:
            return get_next()
    else:
        raise StopIteration

try:
    while True:
        grid[current_y,current_x] = 3
        if current_y+1 >= grid.shape[0]:
            current_y,current_x = get_next()
            continue

        c = grid[current_y+1,current_x]
        if c == 1 or c == 5: # clay or static water
            res1 = spread(current_y,current_x,-1)
            res2 = spread(current_y,current_x,+1)

            if res1 == False and res2 == False:
                # walls on both sides, convert to standing water and move up
                grid[current_y,current_x] = 5
                fill(current_y,current_x,-1)
                fill(current_y,current_x,+1)
                current_y -= 1
            else:
                # if either side is true, do not fill with standing
                # grab the next thing from search
                current_y,current_x = get_next()


        elif c == 0: # empty
            # keep falling
            current_y += 1
        elif c == 3: # flow
            current_y,current_x=get_next()
        else:
            print(f'why did we hit this? {c}')
except StopIteration:
    pass


# rows one and two are not counted in my case
np.savetxt('Day17/gridtest.txt',grid,'%u',' ')
print('part1',np.count_nonzero(np.logical_or(grid==3,grid==5)) - 2)
print('part2',np.count_nonzero(grid==5))
