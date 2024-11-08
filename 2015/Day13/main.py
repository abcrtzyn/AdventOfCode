
import numpy as np
adjacency = np.zeros((8,8))

# I don't think the names change so here they are
people = ['Alice','Bob','Carol','David','Eric','Frank','George','Mallory']


# create an adjacency matrix
with open('Day13/input.txt') as f:
    for line in f.readlines():
        line = line.split()
        pa = line[0]
        pb = line[10].strip('.')
        sign = line[2]
        number = int(line[3]) if sign=='gain' else -int(line[3])
        adjacency[people.index(pa),people.index(pb)] += number
        adjacency[people.index(pb),people.index(pa)] += number

# print(adjacency)

# now just try all the permuatations of 'people'
import itertools

# this would be 8 times faster if Alice was always the first by generality
# it is fast enough right now
bestScore = 0
for perm in itertools.permutations(range(len(people))):
    score = 0
    # sums the circle of distances
    for i in range(len(perm)):
        if i != 7:
            score += adjacency[perm[i],perm[i+1]]
        else:
            score += adjacency[perm[0],perm[i]]
    # picks the largest one
    bestScore = max(bestScore,score)

print('Part 1:',bestScore)

# the difference between part 1 and 2 is that part 2 is about finding the best line rather than circle
bestScore = 0
for perm in itertools.permutations(range(len(people))):
    score = 0
    for i in range(len(perm)-1):
        score += adjacency[perm[i],perm[i+1]]
    
    bestScore = max(bestScore,score)

print('Part 2:',bestScore)
