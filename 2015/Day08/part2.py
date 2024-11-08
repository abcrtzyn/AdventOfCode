total = 0


with open('Day08/input.txt') as f:
    for line in f.readlines():
        # this is a significant refactoring from what I had before
        
        # the answer is the number of backslashes that need to be added
        # to escape the string.
        # the only characters that need to be escaped are \ and "
        # there are also an added " at the beginning and end
        total += 2 + line.count('\\') + line.count('"')
        
print('Part 2:',total)
