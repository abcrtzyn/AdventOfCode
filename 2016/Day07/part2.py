
import re
brackets = re.compile('\\[(.+?)\\]')
outside_brackets = re.compile('(^|\\])(.+?)(\\[|$)')



count = 0
# for each line in the input
# seperate the stuff in brackets
# find all the bab patterns in brackets
# seach for the aba patterns in the non-brackets

with open('Day07/input.txt') as f:
    for line in f.readlines():
        mark = False
        line = line.strip()
        print(line)
        tin = brackets.findall(line)
        tout = outside_brackets.findall(line)

        # search tin segments for bab patterns
        for item in tin:
            for i in range(len(item)-2):
                # aba if 
                if item[i] == item[i+2] and item[i] != item[i+1]:
                    print(f'found {item[i]}{item[i+1]}{item[i+2]}')
                    # search for pattern in outside brackets
                    for _,oitem,_ in tout:
                        if len(re.findall(f'{item[i+1]}{item[i]}{item[i+1]}',oitem)) != 0:
                            #there is a match
                            print('match')
                            count += 1
                            mark = True
                            break
                if mark == True:
                    break
            if mark == True:
                break

print(count)
