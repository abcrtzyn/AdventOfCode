# a list is fine for part 1, but we need something else for part 2
# Im thinking about a linked list to make insertions and removals faster, but 7 million elements still sounds like a lot

# As far as I can tell, there is no easy pattern for the scoring


# 459 players; last marble is worth 72103 points


ring = [0]

# index into the ring
current = 0


def act(n):
    global ring
    global current
    if n % 23 == 0:
        current -= 7
        if current < 0:
            current += len(ring)
        return ring.pop(current) + n
    else:
        current += 2

        if current > len(ring):
            current -= len(ring)
        
        ring.insert(current,n)
        
        return 0



PLAYERS = 459
LAST = 72103

scores = [0] * PLAYERS


i = 0
while True:
    i += 1
    score = act(i)
    if i % 23 == 0:
        scores[(i-1)%PLAYERS] += score
        if i % 23000 == 0:
            print(i)
        # print(i,',',score)
    if i == LAST:
        print(max(scores))
        break
