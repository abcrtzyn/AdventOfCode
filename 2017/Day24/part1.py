# so this is a graph search problem

# each line is an edge, nodes are range from 0 through 50
# the weight of each edge is the sum of the connectors

# find a path starting at node 0 that creates the most value

# recursive depth first search
PART2 = True



import numpy as np

adjacency = np.zeros((51,51),np.int32)
used = np.zeros((51,51),np.bool)



with open('Day24/input.txt') as f:
    for line in f:
        x,y = [int(a) for a in line.split('/')]
        if adjacency[x,y] == 0:
            adjacency[x,y] = x+y
            adjacency[y,x] = x+y
        else:
            # an adjacency matrix must not have the same edge twice
            print('duplicate edge')
            exit(1)


# tries every possible path, returns the best one
def depth_first_search(v:int):
    highest_value = 0
    highest_path = f'{v}'
    for w,e in enumerate(adjacency[v]):
        if e == 0:
            continue
        if used[v,w]:
            continue
        # walk this edge e to node w
        used[v,w] = True
        used[w,v] = True
        # in part 2 individual edge value is one, ties broken for strongest
        ivalue = 1+0.00001*e if PART2 else e
        # with that edge used, pick the higest value path
        value,path = depth_first_search(w)
        if value+ivalue > highest_value:
            highest_value = value + ivalue
            highest_path = f'{v} {path}'
                    
        used[v,w] = False
        used[w,v] = False
    # if no edges were valid, it will return 0 and itself
    return (highest_value,highest_path)



print(depth_first_search(0))
