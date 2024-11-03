from part1 import get_grid



# to count connected regions
# I think we scan the whole thing 
# and skip cells we hare already connected

grid = [x.hex() for x in get_grid('amgozmfv')]

def is_used(x:int,y:int):
    c = grid[x][int(y/4)]

    match y%4:
        case 0:
            return c in ['8','9','a','b','c','d','e','f']
        case 1:
            return c in ['4','5','6','7','c','d','e','f']
        case 2:
            return c in ['2','3','6','7','a','b','e','f']
        case 3:
            return c in ['1','3','5','7','9','b','d','f']


seen = set()

def connect(x,y):
    stack = [(x,y)]
    while len(stack) > 0:
        e = stack.pop()
        seen.add(e)
        # add each neighbor to the queue
        for xof,yof in [(0,1),(0,-1),(1,0),(-1,0)]:
            neighbor = (e[0]+xof,e[1]+yof)
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= 128 or neighbor[1] >= 128:
                continue
            if neighbor in seen:
                continue
            if is_used(neighbor[0],neighbor[1]):
                stack.append(neighbor)



section_count = 0

for i in range(128):
    for j in range(128):
        if (i,j) in seen:
            continue
        if is_used(i,j):
            # put together a connected section
            connect(i,j)
            section_count += 1

print(section_count)
