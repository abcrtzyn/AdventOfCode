

import hashlib

# INPUT STRING HERE
base = 'yzbqklnj'


def solve(base, prefix):
    i=0

    message = ''.join([base,str(i)])

    while not hashlib.md5(bytes(message,'utf8')).digest().hex().startswith(prefix):
        i += 1
        message = ''.join([base, str(i)])
    
    return i


print('Part 1:',solve(base,'00000'))
print('Part 2:',solve(base,'000000'))
