from hashlib import md5
import re

three_rule = re.compile('((\\S)\\2{2,})')
five_rule = re.compile('((\\S)\\2{4,})')

def pad(salt,part2):

    pad_set = set()
    watch_list = {}
    last_i = 40000
    i = 0
    while True:
        s = md5(bytes(salt+str(i),'utf-8'),usedforsecurity=False).hexdigest()
        
        if part2 == True:
            for j in range(2016):
                s = md5(bytes(s,'utf-8'),usedforsecurity=False).hexdigest()

        for m,c in five_rule.findall(s):
            #if len(m) != 5:
            #    continue
            #print(i,c)
            if c in watch_list:
                #print(watch_list[c])
                for n in watch_list[c]:
                    if i <= n+1000:
                        pad_set.add(n)
                        if len(pad_set) == 64:
                            # print('potential last i',n)

                            # n is the 64th or more
                            # finish by checking up to n+1000 for other pads
                            if last_i > n+1000:
                                last_i = n+1000
                del watch_list[c]
                
        mat = three_rule.search(s)    
        if mat is not None:
            m,c = mat.groups()
            #if len(m) != 3:
            #    continue
            # add to watch list
            if c in watch_list:
                if i in watch_list[c]:
                    continue
                watch_list[c].append(i)
            else:
                watch_list[c] = [i]

        i += 1
        if i >= last_i:
            # print(i)
            break
    return pad_set

#SALT = 'abc'
SALT = 'zpqevtbw'

pad_set = pad(SALT,False)
print('Part 1:', sorted(pad_set)[63])
print('part 2 will take a while')
pad_set = pad(SALT,True)
print('Part 2:', sorted(pad_set)[63])
