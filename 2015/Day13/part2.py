
import numpy as np
adjacency = np.zeros((9,9))
people = ['Alice','Bob','Carol','David','Eric','Frank','George','Mallory']


with open('Day13/input.txt') as f:
    for line in f.readlines():
        print(line)
        line = line.split()
        pa = line[0]
        pb = line[10].strip('.')
        sign = line[2]
        number = int(line[3]) if sign=='gain' else -int(line[3])
        print(number)
        adjacency[people.index(pa),people.index(pb)] += number
        adjacency[people.index(pb),people.index(pa)] += number

print(adjacency)

# now just try all the permuatations of 'people'
import itertools

bestScore = 0
for perm in itertools.permutations(range(len(people)+1)):
    score = 0
    for i in range(len(perm)):
        if i != 8:
            score += adjacency[perm[i],perm[i+1]]
        else:
            score += adjacency[perm[0],perm[i]]
    
    #print(perm,score)
    bestScore = max(bestScore,score)
    #break

print(bestScore)