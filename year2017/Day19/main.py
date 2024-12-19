

string = ''
steps = 0

with open('Day19/input.txt') as f:
    grid = f.readlines()

    # get the starting position
    pos = (0,grid[0].index('|'))
    direction = (1,0)

    while True:
        c = grid[pos[0]][pos[1]]
        #print(pos,c)
        match c:
            case '|':
                # keep going
                pass
            case '-':
                # keep going
                pass
            case '+':
                # change direction
                if direction[0] == 0:
                    # vertical to horizontal
                    if grid[pos[0]+1][pos[1]] != ' ':
                        direction = (1,0)
                    elif grid[pos[0]-1][pos[1]] != ' ':
                        direction = (-1,0)
                    else:
                        print('look at',pos,direction)
                else:
                    # horizontal
                    if grid[pos[0]][pos[1]+1] != ' ':
                        direction = (0,1)
                    elif grid[pos[0]][pos[1]-1] != ' ':
                        direction = (0,-1)
                    else:
                        print('look at',pos,direction)
                print(pos,direction)

            case ' ':
                print('space?')
                print(pos,direction)
                break
            case _:
                # letter
                string += c
        
        pos = (pos[0]+direction[0],pos[1]+direction[1])
        steps += 1

print(string)
print(steps)
