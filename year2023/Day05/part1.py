
from typing import List, Tuple


with open('Day05/input.txt') as f:
    seeds = [int(x) for x in f.readline()[7:].split()]
    lines = [x.strip() for x in f.readlines()][:-1]

# split the lines into maps
# if the line is blank, add a new map and skip the next line (header)
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
        maps[-1].append(tuple([int(x) for x in line.split()])) # type: ignore

# maps is a list of lists of range maps

# map the seeds through each map
for m in maps:
    seedsNew = [];
    for seed in seeds:
        for line in m:
            # if the see in in the range of the given line
            if seed >= line[1] and seed < line[1] + line[2]:
                # add the modified value to the list and go to the next seed
                seedsNew.append(seed + line[0] - line[1])
                break;
        else:
            # if no line applies, use the same value
            seedsNew.append(seed)
    # continue with the new values
    seeds = seedsNew;

print('Part 1:',min(seedsNew))
