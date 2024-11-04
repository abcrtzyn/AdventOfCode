
with open('Day05/input.txt') as f:
    inter = [int(x) for x in f.readline()[7:].split()]
    seedRanges = [[inter[i],inter[i+1]] for i in range(0,len(inter),2)]
    
    lines = [x[:-1] for x in f.readlines()][:-1]
    maps = list()
    skip = False
    for line in lines:
        if (line == ''):
            maps.append(list())
            skip = True
        elif (skip):
            skip = False;
            continue
        else:
            maps[-1].append([int(x) for x in line.split()])
            
    # print(seedRanges)
    currentRanges = seedRanges;
    for m in maps:
        newRanges = [];
        for rang in currentRanges:
            for l in m:
                #print(rang[0],rang[0]+rang[1])
                #print(l[1],l[1]+l[2])
                # check for any overlap between l and rang

                # rang is fully within l
                if(l[1] <= rang[0] and rang[0]+rang[1] <= l[1]+l[2]):
                    #print('rang is fully within l')
                    # create mapped range and move to next rang
                    newRanges.append([rang[0]+l[0]-l[1],rang[1]])
                    break;
                #rang is fully outside of l
                elif(rang[0]+rang[1] <= l[1] or l[1]+l[2] <= rang[0]):
                    #print('rang is outside of l')
                    pass;
                elif(rang[0] < l[1]):
                    # the range below the map
                    #print([rang[0],l[1]-rang[0]])
                    currentRanges.append([rang[0],l[1]-rang[0]])
                    #print([l[1],rang[0]+rang[1]-l[1]])
                    newRanges.append([l[1]+l[0]-l[1],rang[0]+rang[1]-l[1]])
                    break;
                elif(rang[0] >= l[1]):
                    #print([l[1]+l[2],rang[0]+rang[1]-l[1]-l[2]])
                    currentRanges.append([l[1]+l[2],rang[0]+rang[1]-l[1]-l[2]])
                    #print([rang[0],l[1]+l[2]-rang[0]])
                    newRanges.append([rang[0]+l[0]-l[1],l[1]+l[2]-rang[0]])
                    break;
                else:
                    raise Exception('missing a case')
                    #print(rang[0],rang[0]+rang[1])
                    #print(l[1],l[1]+l[2])
            else:
                #print(rang[0],rang[0]+rang[1])
                #print('range not found')
                newRanges.append(rang)
        #print(newRanges)
        currentRanges = newRanges;
    print(min([x[0] for x in currentRanges]))
