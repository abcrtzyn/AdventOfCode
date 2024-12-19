edges = dict()

visited = dict()

with open('input.txt','r') as f:
    for line in f:
        edge = tuple(line.strip().split('-'))
        if edge[0] != 'end' and edge[1] != 'start':
            if edge[0] in edges:
                edges[edge[0]].append(edge[1])
            else:
                if edge[0].islower():
                    visited[edge[0]] = False
                edges[edge[0]] = list()
                edges[edge[0]].append(edge[1])
        
        # swap the nodes
        if edge[1] != 'end' and edge[0] != 'start':
            if edge[1] in edges:
                edges[edge[1]].append(edge[0])
            else:
                if edge[1].islower():
                    visited[edge[1]] = False
                edges[edge[1]] = list()
                edges[edge[1]].append(edge[0])

#print(edges)
#print(visited)

paths = 0

def countPaths(node):
    for next in edges[node]:
        if next == 'end':
            global paths
            paths += 1
            continue # try next node
        if next.islower():
            if visited[next]:
                continue # invalid path
            visited[next] = True
        countPaths(next)
        if next.islower():
            visited[next] = False


countPaths('start')
print(paths)
# start at start
# for each true entry in connections grid in the column
    # if end: add to path count return
    # if small, 
    #   if marked return
    #   mark as visited
    # recurse
    # if small
    #   unmark
    # return