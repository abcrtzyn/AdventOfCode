# im going to leave the input text as a list of strings that can be indexed

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3


with open('Day13/input.txt') as f:
    grid = [list(x) for x in f.readlines()]

carts = []
current_coords = set()


# find all the arrows
for i,line in enumerate(grid):
    while True:
        res1 = line.index('<') if '<' in line else -1
        res2 = line.index('>') if '>' in line else -1
        res3 = line.index('^') if '^' in line else -1
        res4 = line.index('v') if 'v' in line else -1
        
        if res1 == -1 and res2 == -1 and res3 == -1 and res4 == -1:
            break
        # handle the arrow
        if res1 != -1:
            grid[i][res1] = '-'
            carts.append((i,res1,LEFT,LEFT))
            current_coords.add((i,res1))
        if res2 != -1:
            grid[i][res2] = '-'
            carts.append((i,res2,RIGHT,LEFT))
            current_coords.add((i,res2))
        if res3 != -1:
            grid[i][res3] = '|'
            carts.append((i,res3,UP,LEFT))
            current_coords.add((i,res3))
        if res4 != -1:
            grid[i][res4] = '|'
            carts.append((i,res4,DOWN,LEFT))
            current_coords.add((i,res4))


def move(y,x,direction):
    match direction:
        case 0: #left
            new_y = y
            new_x = x-1
        case 1: #up
            new_y = y-1
            new_x = x
        case 2: #right
            new_y = y
            new_x = x+1
        case 3: #down
            new_y = y+1
            new_x = x
        case _:
            print('something weird happened',i,y,x,direction,intersection,grid[y][x])
            exit(1)

    current_coords.remove((y,x))
    if (new_y,new_x) in current_coords:
        print('collision',new_x,new_y)
        collided[(new_y,new_x)] = 0
        current_coords.remove((new_y,new_x))

    else:
        current_coords.add((new_y,new_x))
    return (new_y,new_x)

collided = {}
iterations = 0

while len(carts) > 1:
    new_carts = []
    print(carts)
    for i,(y,x,direction,intersection) in enumerate(sorted(carts)):
        # print(i,y,x,direction,intersection)
        if (y,x) in collided:
            collided[(y,x)] += 1
            if collided[(y,x)] == 2:
                del collided[(y,x)]
            continue

        match grid[y][x]:
            case '-':
                if direction == LEFT or direction == RIGHT:
                    y,x = move(y,x,direction)
                    new_carts.append((y,x,direction,intersection))
                else:
                    print('something weird happened',i,y,x,direction,intersection,grid[y][x])
                    exit(1)
            case '|':
                if direction == UP or direction == DOWN:
                    y,x = move(y,x,direction)
                    new_carts.append((y,x,direction,intersection))
                else:
                    print('something weird happened',i,y,x,direction,intersection,grid[y][x])
                    exit(1)
            case '+':
                new_direction = 0
                new_intersection = 0
                match intersection:
                    case 0:
                        new_direction = (direction-1)%4
                        new_intersection = UP
                    case 1:
                        new_direction = direction
                        new_intersection = RIGHT
                    case 2:
                        new_direction = (direction+1)%4
                        new_intersection = LEFT
                    case _:
                        print('something weird happened',i,y,x,direction,intersection,grid[y][x])
                        exit(1)
                y,x = move(y,x,new_direction)
                new_carts.append((y,x,new_direction,new_intersection))

            case '\\':
                match direction:
                    case 0: #left
                        new_direction = UP
                    case 1: #up
                        new_direction = LEFT
                    case 2: #right
                        new_direction = DOWN
                    case 3: #down
                        new_direction = RIGHT
                
                y,x = move(y,x,new_direction)
                new_carts.append((y,x,new_direction,intersection))

            case '/':
                match direction:
                    case 0: #left
                        new_direction = DOWN
                    case 1: #up
                        new_direction = RIGHT
                    case 2: #right
                        new_direction = UP
                    case 3: #down
                        new_direction = LEFT
                
                y,x = move(y,x,new_direction)
                new_carts.append((y,x,new_direction,intersection))

            case _:
                print('something weird happened',i,y,x,direction,intersection,grid[y][x])
                exit(1)

    carts = new_carts
    iterations += 1
    # print(carts)
    # print(iterations)
    # exit(0)
print(carts)
