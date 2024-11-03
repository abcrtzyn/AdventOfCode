
current = []

with open('Day06/input.txt') as f:
    current = [int(x) for x in f.readlines()]

length = len(current)

DP = {}

iterations = 0

while True:

    i = current.index(max(current))
    # remove all from i and redistribute
    v = current[i]
    current[i] = 0
    
    for j in range(1,v+1):
        current[(i+j)%length] += 1
    
    iterations += 1

    if tuple(current) in DP:
        # done
        print('iterations:',iterations)
        print('loop length:',iterations-DP[tuple(current)])
        exit(0)
    
    DP[tuple(current)] = iterations
