from typing import Dict, List

# if the node is not in the list or is printed, it is False
nodes: Dict[int,bool] = {}
# these edges will be backwards from reading order
edges: Dict[int,List[int]] = {}

print_lists: List[List[int]] = []
print_list_fails: List[List[int]] = []

with open('Day05/input.txt') as f:
    mode = 0
    for line in f:
        line = line.strip()
        # print(line.strip())
        if line == '':
            mode += 1
            continue

        if mode == 0:
            # reading edges
            x,y = line.split('|')
            x = int(x)
            y = int(y)
            if x not in nodes:
                nodes[x] = False
            if y not in nodes:
                nodes[y] = False
            if y not in edges:
                edges[y] = []
            edges[y].append(x)
            
        elif mode == 1:
            # reading lists
            print_lists.append([int(x) for x in line.split(',')])

result = 0

for l in print_lists:
    # mark all dependencies as true
    for x in l:
        nodes[x] = True
    try:
        # now check them
        for x in l:
            if x in edges:
                # print('in',x)
                for y in edges[x]:
                    if nodes[y]:
                        # print('edge',x,y)
                        # this dependency is not satisfied, stop now
                        raise Exception('dependency not satified')
                    # else good
            # if x not in edges if fine too
            nodes[x] = False
            
            

        # made it through the list with no issues
        result += l[int(len(l)/2)]
        
    except Exception:
        # reset and go to next list
        for x in l:
            nodes[x] = False
        print_list_fails.append(l)
        

print('Part 1:', result)


# for uniqueness, each list is expected to have one vaild ordering
# the quick and dirty way to find it is to find the one node in the list that comes next
# I'm not familiar with dependncy graphs to know the best of fastest solution
print_list_corrected: List[List[int]] = []


for l in print_list_fails:
    newl = []

    for x in l:
        nodes[x] = True

    # find the next element
    while l:
        for x in l:
            has_dependency = False
            if x in edges:
                    # print('in',x)
                    for y in edges[x]:
                        if nodes[y]:
                            # has dependency
                            has_dependency = True
            
            if not has_dependency:
                break
        nodes[x] = False
        newl.append(x)
        l.remove(x)

    print_list_corrected.append(newl)


result = sum(l[int(len(l)/2)] for l in print_list_corrected)

print('Part 2:', result)
