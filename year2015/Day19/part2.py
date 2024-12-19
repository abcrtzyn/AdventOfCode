# count the number of elements
# when at a open paren [Rn], recurse, stop at Y or Ar
# read part2.txt for more details


def parens(f):
    # count the number of atoms in parentheses
    local_count = 0
    while True:
        a = f.read(1)

        if a.islower():
            # skip lowercase
            continue
        if a == 'Y':
            # y does not get replaced
            local_count -= 1
            continue
        if a == 'A':
            if f.read(1) == 'r':
                # done, minus 1 and return
                local_count -= 1
                return local_count
        # any other atom
        local_count += 1
        if a == 'R':
            f.read(1) # n, discard
            # recurse
            local_count += parens(f)






# the number of atoms in the string, with modifications to how Rn()Ar blocks are handled
count = 0

with open('Day19/text.txt') as f:
    # read characters
    while True:
        a = f.read(1)
        if a == '\n':
            break
        if a.islower():
            # not counting lowercase
            continue

        count += 1
        if a == 'R': # start of an Rn()Ar block
            f.read(1) # n, discard
            count += parens(f)


print('Part 2:',count - 1)
