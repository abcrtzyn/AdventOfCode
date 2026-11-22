from functools import partial
from itertools import combinations
import re
from typing import Dict, Iterable, Iterator, List, Tuple, cast
from python_utils.graph_traversals.shortest_path import a_star

# essentially this is finding a path through a maze with many dimensions
# some cells in the maze are not allowed
# all decisions are reversible

# breadth first search

# (elevator, [(chip 1, gen 1), (chip 2, gen 2)])


# starting at maze state
# we try each combination of movements
# elevator moves up or down one floor
# one or two objects from that floor must move as well

def stuff_on_floor(state: Tuple[int,Tuple[Tuple[int,int],...]]):
    floor = state[0]
    stuff: List[Tuple[int,int]] = []

    for i,(fg,fc) in enumerate(state[1]):
        if fg == floor:
            stuff.append((i,0))
        if fc == floor:
            stuff.append((i,1))

    return stuff

def create_state[T: Tuple[Tuple[int,int],...]](state: Tuple[int,T], direction: bool, items: Iterable[Tuple[int,int]]) -> Tuple[int,T]:
    new_floor = state[0] + (1 if direction else -1)
    
    new_items = [list(x) for x in state[1]]
    for e in items:
        new_items[e[0]][e[1]] = new_floor

    new_items = tuple(sorted(tuple(x) for x in new_items))
    new_state = (new_floor, new_items)
    return cast(Tuple[int,T],new_state)

def check_state(state: Tuple[int,Tuple[Tuple[int,int],...]], old_floor: int):
    # for old_floor and current_floor
    # for each chip on floor
    # if same number generator is not on floor
    # if a generator is on the same floor, invalid state
    
    current_floor = state[0]

    for chip_floor,gen_floor in state[1]:
        if chip_floor == old_floor:
            # if the chip hasn't moved
            if gen_floor != old_floor:
                # and the generator is not on the same floor
                # check for other gens to irradiate it
                for _,gen2_floor in state[1]:
                    if gen2_floor == old_floor:
                        #print(state, f'chip {chip} was irradiated by generator {gen}')
                        # invalid state
                        return False

        if chip_floor == current_floor:
            # if the chip moved to the new floor
            if gen_floor != current_floor:
                # and the generator is not on the same floor
                # check for other gens to irradiate it
                for _,gen2_floor in state[1]:
                    if gen2_floor == current_floor:
                        #print(state, f'chip {chip} was irradiated by generator {gen}')
                        # invalid state
                        return False
    return True



TT = Tuple[int,Tuple[Tuple[int,int],...]]

"""Test states"""
init_stateT = (1,((1,2),(1,3)))
final_stateT = (4,((4,4),(4,4)))


# read the input carefully
# we need to make pairs of floors
microchips: Dict[str,int] = {}
generators: Dict[str,int] = {}

microchips_rule = re.compile(r'a (\w+)-compatible microchip')
generators_rule = re.compile(r'a (\w+) generator')

with open('Day11/input.txt') as f:
    # rather than reading the floor number from the line, just index them
    for floor,line in enumerate(f,1):
        for element in microchips_rule.findall(line):
            microchips[element] = floor
        for element in generators_rule.findall(line):
            generators[element] = floor

if len(microchips) != 5 and 5 != len(generators):
    print('could not find all the microchips or generators')
    print('I am assuming that every input has 5 elements in it')
    exit()


starting_positions = [(microchips[element], generators[element]) for element in microchips]

"""Input states part 1"""
init_state1 = (1,tuple(sorted(starting_positions)))
final_state1 = (4,((4,4),)*5)

# add the two new pairs on floor 1
starting_positions.append((1,1))
starting_positions.append((1,1))

"""Input states part 2"""
init_state2 = (1,tuple(sorted(starting_positions)))
final_state2 = (4,((4,4),)*7)




def get_next_states[T: Tuple[Tuple[int,int],...]](state: Tuple[int,T],current_score: int) -> Iterator[Tuple[int,Tuple[int,T]]]:
    # print(state)
    # I'm using the same approach as before, just in a different way
    stuff = stuff_on_floor(state)
    # print(stuff)
    # for every combination of two items and each item individually
    # try move up and down in the elevator
    # this function will definetly return states that have already been seen, but that is okay
    
    # state_count = 0

    for items in combinations(stuff, 2):
        if state[0] != 4:
            # go up a floor
            new_state = create_state(state, True, items)
            if check_state(new_state,state[0]):
                # state_count += 1
                yield 2,new_state
        ## could comment this next section out,
        ## It would skip checking states where you bring 2 items down
        ## Clear sign of an inefficient solution
        if state[0] != 1:
            # go down a floor
            new_state = create_state(state, False, items)
            if check_state(new_state,state[0]):
                # state_count += 1
                yield 2,new_state

    for item in stuff:
        if state[0] != 4:
            # go up a floor
            new_state = create_state(state, True, [item])
            if check_state(new_state,state[0]):
                # state_count += 1
                yield 2,new_state
        if state[0] != 1:
            # go down a floor
            new_state = create_state(state, False, [item])
            if check_state(new_state,state[0]):
                # state_count += 1
                yield 2,new_state
    
    # print(state,state_count)
                

def compare_states(a: TT, b: TT) -> int:
    """compare the states
    we are just going to do the differences of the floors of the items. Probably will not include elevator level at all
    Oh, and then divide by 2 because 2 things can be moved on the evelator at once."""

    a_items_sum_floors = sum(sum(x) for x in a[1])
    b_items_sum_floors = sum(sum(x) for x in b[1])




    return abs(a_items_sum_floors - b_items_sum_floors)





# res = a_star(cast(TT,init_stateT),lambda x: x == final_stateT,get_next_states,partial(compare_states,final_stateT))
# if res is not None:
#     print('Test:',res//2)
# else:
#     print('no path found for test input')

res = a_star(cast(TT,init_state1),lambda x: x == final_state1,get_next_states,partial(compare_states,final_state1))
if res is not None:
    print('Part 1:',res//2)
else:
    print('no path found for part 1')

res = a_star(cast(TT,init_state2),lambda x: x == final_state2,get_next_states,partial(compare_states,final_state2))
if res is not None:
    print('Part 2:',res//2)
else:
    print('no path found for part 2')
