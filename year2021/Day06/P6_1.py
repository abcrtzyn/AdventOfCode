import numpy as np

def nextState(state):
    s = [0,0,0,0,0,0,0,0,0]
    s[0] = state[1]
    s[1] = state[2]
    s[2] = state[3]
    s[3] = state[4]
    s[4] = state[5]
    s[5] = state[6]
    s[6] = state[7]+state[0]
    s[7] = state[8]
    s[8] = state[0]
    return s

with open('input.txt', 'r') as f:
    values, counts = np.unique([int(number) for number in f.readline().strip().split(',')], return_counts=True)
    frequencies = dict(zip(list(values),list(counts)))
    state = [0,0,0,0,0,0,0,0,0]
    for i in range(0,9):
        try:
            state[i] = frequencies[i]
        except:
            pass
    
    #print(state)
    for i in range(80):
        state = nextState(state)
        #print(state)
    print(sum(state))

    