
def hash(s: str):
    acc1 = 0
    for c in s:
        acc1 += ord(c)
        acc1 *= 17
        acc1 = acc1 % 256
    return acc1

hashtable = []
for i in range(256):
    hashtable.append(list())


with open('Day15/input.txt') as f:
    for step in f.readline().strip().split(','):
        #print(step)
        if step[-1] == '-':
            label = step[:-1]
            key = hash(label)
            # print(key)
            for i in range(len(hashtable[key])):
                if hashtable[key][i][0] == label:
                    hashtable[key].pop(i)
                    break
        else: # =
            label = step[:-2]
            lens = int(step[-1])
            key = hash(label)
            # print(key)
            for i in range(len(hashtable[key])):
                if(hashtable[key][i][0] == label):
                    #print('replacing lens')
                    hashtable[key][i] = (label,lens)
                    break;
            else:
                #print('adding lens')
                hashtable[key].append((label,lens))

score = 0;
for bn, b in enumerate(hashtable):
    for i in range(len(b)):
        p = (bn+1)*(i+1)*b[i][1]
        score += p;

print(score)


        

