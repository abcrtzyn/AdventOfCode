modules = {}

with open('Day20/input.txt') as f:
    for line in f.readlines():
        line = line.strip().split(' -> ')
        #print(line)
        mod = line[0]
        outs = line[1].split(', ')
        tipe = mod[0]
        if tipe != 'b':
            modules[mod[1:]] = (tipe,0,outs)
        else:
            # broadcaster
            modules[mod] = (tipe,0,outs)

# done with the parsing
            
# have to add stsate for all conjunction modules
for module in modules:
    #print(module)
    tipe, state, outs = modules[module]
    #print(tipe,state,outs)
    if tipe == '&':
        state = {}

        for m in modules:
            if module in modules[m][2]:
                state[m] = 0
        modules[module] = (tipe,state,outs)
    
    
first = ('button',0,'broadcaster')
pulseQueue = []

high_count = 0
low_count = 0

for it in range(1000):
    pulseQueue.append(first)
    while len(pulseQueue) != 0:
        source, p, mod = pulseQueue.pop(0)

        # count the pulse
        if p:
            high_count += 1
        else:
            low_count += 1
            
        if mod not in modules:
            continue
        tipe, state, outs = modules[mod]
        #print(source, p,mod,tipe,state)

        newPulse = None
        if tipe == '%':
            if p == 0:
                state = 0 if state else 1
                newPulse = state
                modules[mod] = (tipe,state,outs)

        elif tipe == '&':
            # set the new value
            state[source] = p
            # if all input sources are one
            if 0 in state.values():
                newPulse = 1
            else:
                newPulse = 0
            modules[mod] = (tipe,state,outs)


        elif tipe == 'b':
            newPulse = 0
        
        if newPulse is not None:
            for o in outs:
                pulseQueue.append((mod,newPulse,o))
        


print(high_count*low_count)


        