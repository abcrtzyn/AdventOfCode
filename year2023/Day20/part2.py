## visualization
# https://app.flourish.studio/visualisation/16218805/edit

# there are four sections in the network. Each one is a binary counter with a single conjunction module.
# some of the binary counter flops feed into the conjunction module. These determine the number at which the conjuction module emits a high signal.
# The rest of the modules get a reset signal from the conjuction module so that the whole counter resets to zero on the specific number
# the only way rx gets a low signal is if all 4 counters reach their values at the same time.
# calculations are at the end

modules = {}

with open('Day20/partialinput.txt') as f:
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

# high_count = 0
# low_count = 0
buttons = 0

while True:
    pulseQueue.append(first)
    buttons += 1
    
    while len(pulseQueue) != 0:
        source, p, mod = pulseQueue.pop(0)
        
        #if source == 'jc' and p == 0:
            #print(buttons)
            #raise StopIteration()

        if mod not in modules:
            continue    
            #if p == 0:
        #    print(mod, 'recieved a',p)
        #    print(buttons)
        #    raise StopIteration()
        #    continue
        
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
                if o not in modules:
                    pulseQueue.append((mod,newPulse,o))
                elif not (modules[o][0] == '%' and newPulse == 1):
                    pulseQueue.append((mod,newPulse,o))
    
    if buttons >= 3880:

        l = ['bv','mf','pk','vq','jd','gm','rl','nc','km','fc','vv','vn']
        l.reverse()
        n = 0
        for i in l:
            n = (n << 1) + modules[i][1]
            #print(i,modules[i][1],end=' ')
        #print(buttons, n)
    #print({k: v[1] for k,v in modules.items()})
    if buttons > 7779:
        break
        


# jc is 3889*n
# vm is 3803*n
# fj is 3917*n
# qq is 3877*n
# the answer then is the lcm of these

import math
print(math.lcm(3889,3803,3917,3877))