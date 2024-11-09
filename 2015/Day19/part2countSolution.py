# count the number of elements
# when at a open paren [Rn], recurse, stop at Y or Ar

count = 0

def parens(f):
    local_count = 0
    while True:
        a = f.read(1)

        if a.islower():
            continue
        if a == 'Y':
            local_count -= 1
            continue
        if a == 'A':
            if f.read(1) == 'r':
                # done, minus 1 and return
                local_count -= 1
                # print('Local: ',local_count)
                return local_count
        local_count += 1
        if a == 'R':
            f.read(1) # n, discard
            local_count += parens(f)








with open('Day19/text.txt') as f:
    
    while True:

        a = f.read(1)
        

        if a == '':
            break

        if a.islower():
            continue

        count += 1
        if a == 'R':
            f.read(1) # n, discard
            count += parens(f)

print('Part 2:',count - 2) # minus 1 makes sense, not sure why minus 2
