import collections
from itertools import islice
from typing import Generator, Iterable, List, Literal, Tuple, overload

RULE = [0,1,0,1,1,0,1,0]

@overload
def sliding_window[T](iterable: Iterable[T], n: Literal[3]) -> Generator[Tuple[T,T,T],None,None]: ...
@overload
def sliding_window[T](iterable: Iterable[T], n: Literal[4]) -> Generator[Tuple[T,T,T,T],None,None]: ...

def sliding_window[T](iterable: Iterable[T], n: int) -> Generator[Tuple[T,...],None,None]:
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = collections.deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


#initial = [0,1,1,0,1,0,1,1,1,1]
#rows = 10

with open('Day18/input.txt') as f:
    initial = [1 if c=='^' else 0 for  c in f.read().strip()]
    # print(init_text)
    # exit()

# initial = [0,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1]


def simulate_safe_count(inital: List[int], rows: int):
    row = initial
    safe_count = 0

    safe_count += row.count(0)

    for _ in range(rows-1):
        current: List[int] = []
        # beginning
        current.append(RULE[row[0]*2+row[1]])
        for a,b,c in sliding_window(row,3):
            current.append(RULE[a*4+b*2+c])
        # end
        current.append(RULE[row[-2]*4+row[-1]*2])
        
        safe_count += current.count(0)

        row = current

    return safe_count

print('Part 1:',simulate_safe_count(initial.copy(),40))
print('Part 2:',simulate_safe_count(initial.copy(),400000))
