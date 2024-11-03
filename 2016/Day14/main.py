from hashlib import md5
import re
import heapq

three_rule = re.compile('((\\S)\\2{2,})')
five_rule = re.compile('((\\S)\\2{4,})')

# print(five_rule.findall(md5(b'abc160',usedforsecurity=False).hexdigest()))



# exit(0)

# print(md5(b'abc159',usedforsecurity=False).hexdigest())
# print(md5(b'abc160',usedforsecurity=False).hexdigest())

#SALT = 'abc'
SALT = 'zpqevtbw'

pad_set = set()

watch_list = {}

last_i = 40000
i = 0
while True:
    s = md5(bytes(SALT+str(i),'utf-8'),usedforsecurity=False).hexdigest()
    # PART 2
    # for j in range(2016):
    #     s = md5(bytes(s,'utf-8'),usedforsecurity=False).hexdigest()

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
                        print('potential last i',n)

                        # n is the 64th or more
                        # finish by checking up to n+1000 for other pads
                        if last_i > n+1000:
                            last_i = n+1000
            del watch_list[c]
            
            #print(len(pad_set),pad_set)
        
        

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
        print(i)
        break


print(len(pad_set))

print(sorted(pad_set))
print(sorted(pad_set)[63])
#print(watch_list)
