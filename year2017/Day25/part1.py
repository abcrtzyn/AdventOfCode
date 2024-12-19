states = {
    'A': ((1,'r','B'),(0,'l','E')),
    'B': ((1,'l','C'),(0,'r','A')),
    'C': ((1,'l','D'),(0,'r','C')),
    'D': ((1,'l','E'),(0,'l','F')),
    'E': ((1,'l','A'),(1,'l','C')),
    'F': ((1,'l','E'),(1,'r','A')),
}


current = 'A'
iterations = 12386363
tape = [0]
pos = 0


for _ in range(iterations):
    write, direction, next_state = states[current][tape[pos]]
    tape[pos] = write
    current = next_state
    # move
    if direction == 'l':
        if pos == 0:
            # shift the tape
            tape.insert(0,0)
        else:
            pos -= 1
    else:
        if pos == len(tape)-1:
            tape.append(0)
        pos += 1

print(tape.count(1))
