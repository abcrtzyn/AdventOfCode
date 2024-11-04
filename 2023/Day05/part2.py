
from typing import List, Tuple


with open('Day05/input.txt') as f:
    inter = [int(x) for x in f.readline()[7:].split()]
    seedRanges = [(inter[i],inter[i+1]) for i in range(0,len(inter),2)]
    
    lines = [x.strip() for x in f.readlines()][:-1]


# parse the maps like part 1
maps: List[List[Tuple[int,int,int]]] = list()
skip = False
for line in lines:
    if (line == ''):
        maps.append(list())
        skip = True
    elif (skip):
        skip = False;
        continue
    else:
        maps[-1].append(tuple([int(x) for x in line.split()])) #type: ignore
        

currentRanges = seedRanges;
for m in maps:
    newRanges: List[Tuple[int,int]] = [];
    for rang in currentRanges:
        for l in m:
            # check for any overlap between l and rang

            if(l[1] <= rang[0] and rang[0]+rang[1] <= l[1]+l[2]):
                # rang is fully within l
                # create mapped range and move to next rang
                newRanges.append((rang[0]+l[0]-l[1],rang[1]))
                break;
            elif(rang[0]+rang[1] <= l[1] or l[1]+l[2] <= rang[0]):
                #rang is fully outside of l
                pass;
            elif(rang[0] < l[1]):
                # the range partially below the map
                currentRanges.append((rang[0],l[1]-rang[0])) # check this part for a different range
                newRanges.append((l[1]+l[0]-l[1],rang[0]+rang[1]-l[1]))
                break;
            elif(rang[0] >= l[1]):
                # the range is partially above the map
                currentRanges.append((l[1]+l[2],rang[0]+rang[1]-l[1]-l[2])) # check this part for a different range
                newRanges.append((rang[0]+l[0]-l[1],l[1]+l[2]-rang[0]))
                break;
            else:
                raise AssertionError('missing a case')
        else:
            # no range map found, pass all values on with no change
            newRanges.append(rang)

    # loop again with new ranges
    currentRanges = newRanges;

print('Part 2:', min([x[0] for x in currentRanges]))
