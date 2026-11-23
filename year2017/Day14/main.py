
from typing import List, Set, Tuple

from year2017.Day10.main import knothash


with open('Day14/input.txt') as f:
    KEY = f.readline().strip()


def get_grid(key: str):
    for i in range(128):
        yield knothash(bytes(key + '-' + str(i),'ascii'))


grid = list(int.from_bytes(x) for x in get_grid(KEY))

count = 0

for row in grid:
    count += row.bit_count()
        
print('Part 1:',count)

# for line in grid:
#     print(f'{line:0128b}')
# exit()

def is_used(x:int,y:int):
    # is this coordinate a 1 in the bit
    r = grid[x]
    # bit mask time
    # 0 is most significant, 127 is least significant
    c = r & (1 << (127-y))
    
    return c != 0


seen: Set[Tuple[int,int]] = set()

def connect(x: int,y: int):
    stack: List[Tuple[int,int]] = [(x,y)]
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

print('Part 2:',section_count)
