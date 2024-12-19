from hashlib import md5

key = 'veumntbg'
#key = 'ihgpwlah'


# yet another time to implement a*

# implementating A* for this task

from functools import partial
import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Entry:
    priority: int
    path: Any=field(compare=False)


goal = (4,4)

def get_coord(path):
    x = 1
    y = 1
    for c in path:
        match c:
            case 'U': y -= 1
            case 'D': y += 1
            case 'L': x -= 1
            case 'R': x += 1
            case _:
                print('not a direction character')
                exit(1)
    return (x,y)

# taxicab distance
def taxicab(a,b):
    return abs(a[0]-b[0])+abs(a[1]+b[1])



def max_path(path='',coord=(1,1)):

    if coord == goal:
        print(len(path))
        return (len(path),path)

    hsh = md5(bytes(key+path,'utf-8')).hexdigest()[:4]

    max_len = 0
    max_pathh = ''

    

    for npath,ncoord,nch in zip([path+'U',path+'D',path+'L',path+'R'],
                                [(coord[0],coord[1]-1),(coord[0],coord[1]+1),(coord[0]-1,coord[1]),(coord[0]+1,coord[1])],
                                 hsh):

        if ncoord[0] < 1 or ncoord[1] < 1:
            continue
        if ncoord[0] > 4 or ncoord[1] > 4:
            continue
        if ord(nch) < 98:
            continue

        ten_len, ten_path = max_path(npath,ncoord)
        if ten_len > max_len:
            max_len = ten_len
            max_pathh = ten_path
    
    return (max_len, max_pathh)




        




print(max_path())
