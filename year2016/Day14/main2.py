# My previous solution was actually like, pretty bad, at least memory wise
# This solution, I'm just going to maintain a 1000 item list
# the list is basically a rotating buffer of the past 1000 items triplet value

# if a hash has the 5 of a kind
# we iterate through the list, add any with that symbol to the count


from hashlib import md5
import re
from typing import List


three_rule = re.compile('((\\S)\\2{2,})')
five_rule = re.compile('((\\S)\\2{4,})')

def pad(salt: str,part2: bool):
    # this is the list of the last 1000 filter characters
    watch_list: List[str] = [''] * 1000
    # this is the number of valid pads so far
    number_of_pad = 0
    
    i = -1
    while True:
        i += 1
        s = md5(bytes(salt+str(i),'utf-8'),usedforsecurity=False).hexdigest()
        # if part 2, do another 2016 hashes
        if part2 == True:
            for _ in range(2016):
                s = md5(bytes(s,'utf-8'),usedforsecurity=False).hexdigest()

        # if there is a 5 in a row, we need to count the last 1000 with the same filter
        last_candidates: List[int] = []
        for _,c in five_rule.findall(s):
            # check the last 1000
            for j,d in enumerate(watch_list):
                if c == d:
                    # if the charecter is the some
                    watch_list[j] = '' # reset the index (to not double count it)
                    number_of_pad += 1 # add to the pad count
                    # figure out which real index we just added
                    if j >= i % 1000:
                        last_candidates.append((i - i % 1000 - 1000) + j)
                    else:
                        last_candidates.append((i - i % 1000) + j)
        
        if number_of_pad >= 64:
            # if we have finished, figure out what the 64th index is
            last_candidates.sort()
            sixtyforth = last_candidates[-(number_of_pad-64+1)]
            return sixtyforth

        # if there is a 3 in a row, add it to the watch list
        mat = three_rule.search(s)    
        if mat is not None:
            _,c = mat.groups()
            # add to watch list
            watch_list[i % 1000] = c
        else:
            watch_list[i % 1000] = ''



#SALT = 'abc'
with open('Day14/input.txt') as f:
    SALT = f.read().strip()

print('Part 1:', pad(SALT,False))
print('part 2 will take a while')
print('Part 2:', pad(SALT,True))

