from itertools import combinations

# essentially this is finding a path through a maze with many dimensions
# some cells in the maze are not allowed
# all decisions are reversible

# breadth first search

# (elevator, (chip 1, chip 2), (gen 1, gen 2))


# starting at maze state
# we try each combination of movements
# elevator moves up or down one floor
# one or two objects from that floor must move as well

def stuff_on_floor(state):
    floor = state[0]
    stuff = []

    for i,f in enumerate(state[1]):
        if f == floor:
            stuff.append((0,i))
    for i,f in enumerate(state[2]):
        if f == floor:
            stuff.append((1,i))
    
    return stuff

def create_state(state, direction, items):
    new_floor = state[0] + (1 if direction else -1)
    
    new_items = [list(state[1]), list(state[2])]
    for e in items:
        new_items[e[0]][e[1]] = new_floor
    
    new_state = (new_floor, tuple(new_items[0]),tuple(new_items[1]))
    return new_state

def check_state(state, old_floor):
    # for old_floor and current_floor
    # for each chip on floor
    # if same number generator is not on floor
    # if a generator is on the same floor, invalid state
    
    current_floor = state[0]

    for chip,chip_floor in enumerate(state[1]):
        if chip_floor == old_floor:
            if state[2][chip] != old_floor:
                # check for other gens
                for gen,gen_floor in enumerate(state[2]):
                    if gen_floor == old_floor:
                        #print(state, f'chip {chip} was irradiated by generator {gen}')
                        # invalid state
                        return False

        if chip_floor == current_floor:
            if state[2][chip] != current_floor:
                # check for other gens
                for gen,gen_floor in enumerate(state[2]):
                    if gen_floor == current_floor:
                        #print(state, f'chip {chip} was irradiated by generator {gen}')
                        # invalid state
                        return False
    return True


def solve(init_state, final_state):
    DP = {}
    queue = []

    queue.append((init_state,0))
    steps = 0
    while len(queue) > 0:
        old_steps = steps
        maze_state, steps = queue.pop(0)
        # if steps > old_steps:
            # print(steps, len(queue)+1)

        if maze_state in DP:
            continue

        DP[maze_state] = steps
        current_floor = maze_state[0]

        # make a list of everything on floor 1
        stuff = stuff_on_floor(maze_state)


        new_found = False
        # move 2 things
        for items in combinations(stuff, 2):
            if current_floor != 4:
                # go up a floor
                new_state = create_state(maze_state, True, items)
                if new_state not in DP and check_state(new_state,current_floor):
                    # add to queue
                    new_found = True
                    if new_state == final_state:
                        return steps+1
                    queue.append((new_state,steps+1))


        down_accceptable = False
        for x,y in zip(maze_state[1],maze_state[2]):
            if x < current_floor or y < current_floor:
                down_accceptable = True
                break

        for item in stuff:
            if current_floor != 1 and down_accceptable:
                

                # go down a floor
                new_state = create_state(maze_state, False, [item])
                if new_state not in DP and check_state(new_state,current_floor):
                    # add to queue
                    if new_state == final_state:
                        return steps+1
                    
                    queue.append((new_state,steps+1))

        if not new_found:
            #print('run')
            for item in stuff:
                if current_floor != 4:
                    # go up a floor
                    new_state = create_state(maze_state, True, [item])
                    if new_state not in DP and check_state(new_state,current_floor):
                        # add to queue
                        new_found = True
                        if new_state == final_state:
                            return steps+1
                        queue.append((new_state,steps+1))

"""Test states"""
init_stateT = (1,(1,1),(2,3))
final_stateT = (4,(4,4),(4,4))
"""Input states part 1"""
init_state1 = (1,(1,2,3,1,2),(1,2,2,1,2))
final_state1 = (4,(4,4,4,4,4),(4,4,4,4,4))
"""Input states part 2"""
init_state2 = (1,(1,2,3,1,2,1,1),(1,2,2,1,2,1,1))
final_state2 = (4,(4,4,4,4,4,4,4),(4,4,4,4,4,4,4))

# solve(init_stateT,final_stateT)
print('Part 1:',solve(init_state1,final_state1))
print('part 2 takes a while')
print('Part 2:',solve(init_state2,final_state2))
