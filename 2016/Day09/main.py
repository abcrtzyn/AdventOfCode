
from io import StringIO


PART2 = True

def uncompress(buf) -> int:
    count = 0
    while True:

        c = buf.read(1)

        match c:
            case '':
                return count
            case '\n':
                continue
            case '(':
                # handle a compression marker
                count += compression_marker(buf)
            case _:
                count += 1


# figures out the length of the text inside the compression zone
# returns it
def compression_marker(f):
    # start a compression marker
    num = ''
    c = f.read(1)
    # read until 'x' (number of characters)
    while c != 'x':
        num = num + c
        c = f.read(1)
    
    num_chars = int(num)

    # read until ')' (number of repetitions)
    num = ''
    c = f.read(1)
    while c != ')':
        num = num + c
        c = f.read(1)
    
    repitions = int(num)
    
    """
    part 1 skips over compressed blocks
    part 2 handles recursion
    """
    if PART2:
        sub = f.read(num_chars)
        if len(sub) != num_chars:
            exit(1)
        uncompressed_chars = uncompress(StringIO(sub))
        return uncompressed_chars * repitions
    else:
        f.read(num_chars) # skip past the rest
        return num_chars * repitions
        

with open('Day09/input.txt') as f:
    print(uncompress(f))
    exit(0)
