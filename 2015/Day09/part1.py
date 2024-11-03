
places = ['Tristram','AlphaCentauri','Snowdin','Tambi','Faerun','Norrath','Straylight','Arbre']
#places = ['Dublin','London','Belfast']

import numpy as np

dist = np.zeros((len(places),len(places)))


with open('Day09/input.txt') as f:
    for line in f.readlines():
        line = line.split()
        print(line)
        i = places.index(line[0])
        j = places.index(line[2])
        dist[i,j] = int(line[4])
        dist[j,i] = int(line[4])

print(dist)


def calculateDistance(used,previous):
    # go through the list, take the first false one
    mindist = 10000000
    for i in range(len(places)):
        if not used[i]:
            used[i] = True
            if previous is not None:
                mindist = min(mindist,dist[previous,i]+calculateDistance(used,i))
            else:
                mindist = min(mindist,calculateDistance(used,i))
            used[i] = False
    
    if mindist == 10000000:
        return 0
    return mindist

print(calculateDistance([False]*len(places),None))