
# MAKE SURE YOUR PLACES ARE THE SAME
places = ['Tristram','AlphaCentauri','Snowdin','Tambi','Faerun','Norrath','Straylight','Arbre']
#places = ['Dublin','London','Belfast']

import numpy as np

dist = np.zeros((len(places),len(places)))


with open('Day09/input.txt') as f:
    for line in f.readlines():
        line = line.split()
        
        i = places.index(line[0])
        j = places.index(line[2])
        dist[i,j] = int(line[4])
        dist[j,i] = int(line[4])


# essentially depth first search on all paths
# standard backtracking done a little crudely
# used is a list that marks used locations
# previous is the previous location, None for the first
# f is the superlative function (max or min)
# default is the default dummy distance value

# the function returns 0 if no path is more superlative than the default value
# otherwise returns the most superlative path length

def calculateDistance(used,previous,f,default):
    # go through the list, take the first false one
    superlative_dist = default
    
    for i in range(len(places)):
        if not used[i]:
            used[i] = True
            if previous is not None:
                superlative_dist = f(superlative_dist,dist[previous,i]+calculateDistance(used,i,f,default))
                
            else:
                superlative_dist = f(superlative_dist,calculateDistance(used,i,f,default))
                
            used[i] = False
    
    if superlative_dist == default:
        return 0
    return superlative_dist


print('Part 1:',calculateDistance([False]*len(places),None,min,100000000))
print('Part 2:',calculateDistance([False]*len(places),None,max,0))
