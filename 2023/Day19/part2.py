workflows = {}

slices = []

with open('Day19/input.txt') as f:
    emptyline = False

    for line in f.readlines():
        line = line.strip()
        if line == '':
            break
        
        i = line.find('{')
        flow = line[0:i]
        line = line[i+1:-1] # gets rid of the {}
        steps = line.split(',')
        final = steps[-1]
        steps = [step.split(':') for step in steps[:-1]]
        steps = [(step[0][0],step[0][1],int(step[0][2:]),step[1]) for step in steps]
        steps.append(('m','>',0,final)) # unconditional final stage
        workflows[flow] = steps;

#print(workflows)

def countSlice(slice):
    return (slice['x'][1]-slice['x'][0])*(slice['m'][1]-slice['m'][0])*(slice['a'][1]-slice['a'][0])*(slice['s'][1]-slice['s'][0])

def function(flow,i,slice:dict):
    score = 0
    # each step in the workflow splits the slice (maybe) into two slices.
    step = workflows[flow][i]
    #print(slice)
    #print(slice,flow, i, step)
    
    if slice[step[0]][0] <= step[2] and step[2] < slice[step[0]][1]:
        # the step splits the slice
        moveslice = slice.copy()
        stayslice = slice.copy()
        if step[1] == '<':
            moveslice[step[0]] = (slice[step[0]][0],step[2])
            stayslice[step[0]] = (step[2],slice[step[0]][1])
        elif step[1] == '>':
            moveslice[step[0]] = (step[2]+1,slice[step[0]][1])
            stayslice[step[0]] = (slice[step[0]][0],step[2]+1)

        #print(moveslice, stayslice)
        if step[3] == 'A':
            score += countSlice(moveslice)
        elif step[3] == 'R':
            pass
        else:
            score += function(step[3],0,moveslice)
        
        score += function(flow,i+1,stayslice)
    else:
        # the slice does not split
        #print(slice)
        if (step[2] < slice[step[0]][0] and step[1] == '>') or (step[2] >= slice[step[0]][1] and step[1] == '<'):
            # slice moves
            if step[3] == 'A':
                score += countSlice(slice)
            elif step[3] == 'R':
                pass
            else:
                score += function(step[3],0,slice)
            
        elif (step[2] < slice[step[0]][0] and step[1] == '<') or (step[2] >= slice[step[0]][1] and step[1] == '>'):
            # slice stays
            score += function(flow,i+1,slice)
        else:
            raise Exception('havent thought about this yet')
        

    return score
    
    
    

fullslice = {'x':(1,4001),'m':(1,4001),'a':(1,4001),'s':(1,4001)}

print(function('in',0,fullslice))

