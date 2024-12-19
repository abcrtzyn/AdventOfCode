# a list is fine for part 1, but we need something else for part 2
# Im thinking about a linked list to make insertions and removals faster, but 7 million elements still sounds like a lot
# WOW, linked list in a hash table is amazing.


# As far as I can tell, there is no easy pattern for the scoring


# 459 players; last marble is worth 72103 points

from typing import Dict, Tuple


links: Dict[int,Tuple[int,int]] = {}
# A link will store the previous and next

links[0] = (0,0)

def next(n):
    return links[n][1]

def prev(n):
    return links[n][0]

# insert x where n currently is
def insert(x, n):
    p = prev(n)
    # update the links, n becomes the next
    links[p] = (links[p][0],x)
    links[x] = (p,n)
    links[n] = (x,links[n][1])

def remove(x):
    p = prev(x)
    n = next(x)
    links[p] = (links[p][0],n)
    links[n] = (p,links[n][1])


PLAYERS = 459
LAST = 7210300

scores = [0] * PLAYERS

current = 0
i = 0
while True:
    i += 1
    
    if i % 23 == 0:
        # do something fun
        current = prev(prev(prev(prev(prev(prev(current))))))
        score = i + links[current][0]
        remove(links[current][0])
        scores[(i-1)%PLAYERS] += score
        if i % 230000 == 0:
            print(i)
    else:
        # move the current two forward
        current = next(next(current))
        # then insert i
        insert(i,current)
        current = i

    if i == LAST:
        break

print(max(scores))
