import hashlib

base = 'uqwqemis'
i=-1
j = 0
password = {}
valids = ['0','1','2','3','4','5','6','7']
while j != 8:
    h = '11111'
    while not h.startswith('00000'):
        i += 1
        message = ''.join([base, str(i)])
        h = hashlib.md5(bytes(message,'utf8')).digest().hex()
    if h[5] in valids and h[5] not in password:
        password[h[5]] = h[6]
        j += 1
    
    # print(i)
    # print(h[5],h[6])

print('Part 2: ',end='')
for a in valids:
    print(password[a],end='')
print()
# print(password)
