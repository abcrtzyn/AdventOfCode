import hashlib

base = 'uqwqemis'
i=-1
j = 0
password = ''
while j != 8:
    h = '11111'
    while not h.startswith('00000'):
        i += 1
        message = ''.join([base, str(i)])
        h = hashlib.md5(bytes(message,'utf8')).digest().hex()
    password += h[5]
    j += 1
    
    # print(i)
    # print(h[5])

print('Part 1:',password)
