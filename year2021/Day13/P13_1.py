import numpy as np
import re
points = list()

foldInstructions = False
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if foldInstructions:
            # parse line
            match = re.fullmatch('fold along (?P<axis>.)=(?P<number>.+)', line)
            foldDirection = 0
            if match.groups()[0] == 'y':
                foldDirection = 1
            value = int(match.groups()[1])
            
            for point in points:
                if point[foldDirection] > value:
                    point[foldDirection] = 2 * value - point[foldDirection]
            #print(len(points))
            #reduce
            points = np.unique(points, axis=0)
            print(points.shape)
            break

        elif line == '':
            points = np.array(points)
            foldInstructions = True
        else:
            points.append(list([int(s) for s in line.split(',')]))

