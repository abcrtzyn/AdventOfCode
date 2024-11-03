import collections
from itertools import islice

RULE = [0,1,0,1,1,0,1,0]

def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = collections.deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


#initial = [0,1,1,0,1,0,1,1,1,1]
#rows = 10
initial = [0,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1]
rows = 40

safe_count = 0

row = initial

safe_count += row.count(0)

for i in range(rows-1):
    current = []
    # beginning
    current.append(RULE[row[0]*2+row[1]])
    for a,b,c in sliding_window(row,3):
        current.append(RULE[a*4+b*2+c])
    # end
    current.append(RULE[row[-2]*4+row[-1]*2])
    
    safe_count += current.count(0)

    row = current

print(safe_count)
