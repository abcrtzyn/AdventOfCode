
# dykstras algorithm with the following states (x,y,direction,steps of direction)

DOWN = (1, 0)
UP = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

TURNLEFT = {UP: LEFT, DOWN: RIGHT, LEFT: DOWN, RIGHT: UP}
TURNRIGHT = {UP: RIGHT, DOWN: LEFT, LEFT: UP, RIGHT: DOWN}
DIRMAP = {DOWN: 0, UP: 1, LEFT: 2, RIGHT: 3}

import numpy as np

with open('Day17/input.txt') as f:
    grid = np.array([[int(y) for y in x.strip()] for x in f.readlines()])
SIZE = grid.shape[0]

costs = np.ones((SIZE,SIZE,4,3),np.int32)*178929

def readCosts(v):
    return costs[v[0],v[1],DIRMAP[v[2]],v[3]-1]

def writeCosts(v,n):
    costs[v[0],v[1],DIRMAP[v[2]],v[3]-1] = n;


# handles things where the costs are in a seperate thing
class HeapState:

    def __init__(self):
        self.container = list()
    
    def __len__(self):
        return len(self.container)

    def _siftdown(self, start, current):
        newitem = self.container[current]

        while current > start:
            parent = (current - 1) >> 1
            parentitem = self.container[parent]
            if readCosts(newitem) < readCosts(parentitem):
                self.container[current] = parentitem
                current = parent
                continue
            break
        self.container[current] = newitem

    def _siftup(self, current):
        end = len(self)
        start = current
        newitem = self.container[current]
        child = 2*current+1
        while child < end:
            right = child+1
            if right < end and not readCosts(self.container[child]) < readCosts(self.container[right]):
                child = right
            self.container[current] = self.container[child]
            current = child
            child = 2*current + 1
        self.container[current] = newitem
        self._siftdown(start, current)

    def push(self, item):
        self.container.append(item)
        self._siftdown(0, len(self)-1)

    def pop(self):
        last = self.container.pop() # raises empty error
        if self.container:
            ret = self.container[0]
            self.container[0] = last
            self._siftup(0)
            return ret
        return last
    
    def poppush(self, item):
        ret = self.container[0]
        self.container[0] = item
        self._siftup(0)
        return ret
    
    def pushpop(self, item):
        if self.container and readCosts(self.container[0]) < readCosts(item):
            item, self.container[0] = self.container[0], item
            self._siftup(0)
        return item


heap = HeapState()

def rangeCheck(x,y):
    return 0 <= x and x < SIZE and 0 <= y and y < SIZE


writeCosts((1,0,DOWN,1),grid[1,0])
writeCosts((0,1,RIGHT,1),grid[0,1])

heap.push((1,0,DOWN,1))
heap.push((0,1,RIGHT,1))

ite = 0
while len(heap) > 0:
    cur = heap.pop()
    y,x,di,s = cur
    cost = readCosts(cur)
    if x == SIZE-1 and y == SIZE-1:
        print('got the end in', cost, ite)
        break
    
    # print('working on',((y,x,di,s),cost))

    # try all three directions

    # straight
    if s < 3:
        sty = y + di[0]
        stx = x + di[1]
        if rangeCheck(stx,sty):
            newV = (sty,stx,di,s+1)
            newCost = cost + grid[sty,stx]
            if readCosts(newV) > newCost:
                writeCosts(newV,newCost)

                if newV in heap.container:
                    # replace the cost on the old one with this one
                    # heap.container[i] = (newV,newCost)
                    # heap._siftdown(0,i)
                    raise Exception('not implemented')
                else:
                    # print('adding    ', (newV,newCost))
                    heap.push(newV)
    
    # left
    ledi = TURNLEFT[di]
    ley = y + ledi[0]
    lex = x + ledi[1]
    if rangeCheck(lex,ley):
        newV = (ley,lex,ledi,1)
        newCost = cost + grid[ley,lex]
        if readCosts(newV) > newCost:
            writeCosts(newV,newCost)

            if newV in heap.container:
                # replace the cost on the old one with this one
                # heap.container[i] = (newV,newCost)
                # heap._siftdown(0,i)
                raise Exception('not implemented')
            else:
                # print('adding    ', (newV,newCost))
                heap.push(newV)

    # right
    ridi = TURNRIGHT[di]
    riy = y + ridi[0]
    rix = x + ridi[1]
    if rangeCheck(rix,riy):
        newV = (riy,rix,ridi,1)
        newCost = cost + grid[riy,rix]
        if readCosts(newV) > newCost:
            writeCosts(newV,newCost)

            if newV in heap.container:
                # replace the cost on the old one with this one
                # heap.container[i] = (newV,newCost)
                # heap._siftdown(0,i)
                raise Exception('not implemented')
            else:
                # print('adding    ', (newV,newCost))
                heap.push(newV)

    ite+=1
    #if ite > 1000:
    #    break
