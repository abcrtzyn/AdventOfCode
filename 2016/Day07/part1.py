import re
brackets = re.compile('\\[(.+?)\\]')
outside_brackets = re.compile('(^|\\])(.+?)(\\[|$)')


def findabba(s: str) -> bool:
    for i in range(len(s)-3):
        # abba if 
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False


count = 0
with open('Day07/input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        #print(line)
        # have to split out the sections of []
        m = brackets.findall(line)
        # for each item in list m
        # figure out if there is a pattern
        for a in m:
            #print(a)
            if findabba(a):
                # this ip is invalid
                break
        else:
            # no square bracket pass
            # now for the rest
            m = outside_brackets.findall(line)
            for _,a,_ in m:
                #print(a)
                if findabba(a):
                    count += 1
                    break
            
        
print(count)
