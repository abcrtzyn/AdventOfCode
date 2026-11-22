from functools import partial
from itertools import combinations
from typing import Iterable, Iterator, List, Tuple, cast
from python_utils.graph_traversals.shortest_path import a_star

# essentially this is finding a path through a maze with many dimensions
# some cells in the maze are not allowed
# all decisions are reversible

# breadth first search

# (elevator, (chip 1, chip 2), (gen 1, gen 2))


# starting at maze state
# we try each combination of movements
# elevator moves up or down one floor
# one or two objects from that floor must move as well

def stuff_on_floor(state: Tuple[int,Tuple[int,...],Tuple[int,...]]):
    floor = state[0]
    stuff: List[Tuple[int,int]] = []

    for i,f in enumerate(state[1]):
        if f == floor:
            stuff.append((0,i))
    for i,f in enumerate(state[2]):
        if f == floor:
            stuff.append((1,i))
    
    return stuff

def create_state[T: Tuple[int,...]](state: Tuple[int,T,T], direction: bool, items: Iterable[Tuple[int,int]]) -> Tuple[int,T,T]:
    new_floor = state[0] + (1 if direction else -1)
    
    new_items = [list(state[1]), list(state[2])]
    for e in items:
        new_items[e[0]][e[1]] = new_floor
    
    new_state = (new_floor, tuple(new_items[0]),tuple(new_items[1]))
    return cast(Tuple[int,T,T],new_state)

def check_state(state: Tuple[int,Tuple[int,...],Tuple[int,...]], old_floor: int):
    # for old_floor and current_floor
    # for each chip on floor
    # if same number generator is not on floor
    # if a generator is on the same floor, invalid state
    
    current_floor = state[0]

    for chip,chip_floor in enumerate(state[1]):
        if chip_floor == old_floor:
            if state[2][chip] != old_floor:
                # check for other gens
                for generation,gen_floor in enumerate(state[2]): # pyright: ignore[reportUnusedVariable]
                    if gen_floor == old_floor:
                        #print(state, f'chip {chip} was irradiated by generator {gen}')
                        # invalid state
                        return False

        if chip_floor == current_floor:
            if state[2][chip] != current_floor:
                # check for other gens
                for generation,gen_floor in enumerate(state[2]): # pyright: ignore[reportUnusedVariable]
                    if gen_floor == current_floor:
                        #print(state, f'chip {chip} was irradiated by generator {gen}')
                        # invalid state
                        return False
    return True



TT = Tuple[int,Tuple[int,int],Tuple[int,int]]
T1 = Tuple[int,Tuple[int,int,int],Tuple[int,int,int]]
T2 = Tuple[int,Tuple[int,int,int,int],Tuple[int,int,int,int]]


"""Test states"""
init_stateT = (1,(1,1),(2,3))
final_stateT = (4,(4,4),(4,4))
"""Input states part 1"""
init_state1 = (1,(1,2,3,1,2),(1,2,2,1,2))
final_state1 = (4,(4,4,4,4,4),(4,4,4,4,4))
"""Input states part 2"""
init_state2 = (1,(1,2,3,1,2,1,1),(1,2,2,1,2,1,1))
final_state2 = (4,(4,4,4,4,4,4,4),(4,4,4,4,4,4,4))

def get_next_states[T: Tuple[int,...]](state: Tuple[int,T,T],current_score: int) -> Iterator[Tuple[int,Tuple[int,T,T]]]:
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
        ## this is commented out, I am enforecing a ideal that you are never allowed
        ## to bring two items down. Sign of an inefficient solution
        # if state[0] != 1:
        #     # go down a floor
        #     new_state = create_state(state, False, items)
        #     if check_state(new_state,state[0]):
        #         state_count += 1
        #         yield 2,new_state

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
                

def compare_states(a: Tuple[int,Tuple[int,...],Tuple[int,...]], b: Tuple[int,Tuple[int,...],Tuple[int,...]]) -> int:
    """compare the states
    we are just going to do the differences of the floors of the items. Probably will not include elevator level at all
    Oh, and then divide by 2 because 2 things can be moved on the evelator at once."""

    a_chips = a[1]
    a_gens = a[2]
    b_chips = b[1]
    b_gens = b[2]



    return abs((sum(a_chips) - sum(b_chips)) + (sum(a_gens) - sum(b_gens)))





# solve(init_stateT,final_stateT)
# res = a_star(cast(TT,init_stateT),lambda x: x == final_stateT,get_next_states,partial(compare_states,final_stateT))
# if res is not None:
#     print('Test:',res//2)
# else:
#     print('no path found for test input')

res = a_star(cast(T1,init_state1),lambda x: x == final_state1,get_next_states,partial(compare_states,final_state1))
if res is not None:
    print('Part 1:',res//2)
else:
    print('no path found for part 1')

res = a_star(cast(T2,init_state2),lambda x: x == final_state2,get_next_states,partial(compare_states,final_state2))
if res is not None:
    print('Part 2:',res//2)
else:
    print('no path found for part 2')
