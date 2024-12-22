# An interesting challenge
# first, as an example, there are multiple ways to get from 2 to 9
# but after one level of indirection, it could be better to go a different way

# in basic terms, it is a search problem

# other things that matter
# A robot moving from 9 to A will yeild the same number of steps

# to press each button, the next robot must press the A button
# for each digit in the code, all robots are on the A buttone
# It is not an easy fact to think about

from typing import Dict, List, Tuple
from graph_traversals.breadth_first_search import breadth_first_search, breadth_first_search_parents

from functools import partial

numpad_neighbors_dict = {
    '7': {'4':'v','8':'>'},         '8': {'5':'v','7':'<','9':'>'},         '9': {'6':'v','8':'<'},
    '4': {'1':'v','5':'>','7':'^'}, '5': {'2':'v','4':'<','6':'>','8':'^'}, '6': {'3':'v','5':'<','9':'^'},
    '1': {'2':'>','4':'^'},         '2': {'0':'v','1':'<','3':'>','5':'^'}, '3': {'2':'<','6':'^','A':'v'},
                                    '0': {'2':'^','A':'>'},                 'A': {'0':'<','3':'^'},
}

arrow_neighbors_dict = {
                    '^':{'v':'v','A':'>'},         'A':{'^':'<','>':'v'},
    '<':{'v':'>'},  'v':{'<':'<','^':'^','>':'>'}, '>':{'A':'^','v':'<'},
}

def is_pushed(x: Tuple[str,str]):
    return x[0] == 'P'


def indirect_entry_neighbors(next_neighbors_func, neighbors: Dict[str,Dict[str,str]], goal: str, current: Tuple[str,str], score: int):
    # print('1st',goal,current,score)
    if current[0] == goal:
        # go to and press A
        result = breadth_first_search((current[1],'A'), is_pushed, partial(next_neighbors_func,'A'))
        if result is None:
            print(f'no path found from {current} to {goal}???')
            exit(1)
        # print('1st',current,('pushed','A'),result,score+result)
        yield (score+result,('P','A'))
    
    else:
        for neigh,in_neigh in neighbors[current[0]].items():
            # go to the symbol at neighbors[c][n] and press it
            result = breadth_first_search((current[1],'A'), is_pushed, partial(next_neighbors_func,in_neigh))
            if result is None:
                print(f'no path found from {current} to {neigh}???')
                exit(1)
            # print('1st',current,(neigh,in_neigh),result,score+result)
            yield (score+result,(neigh,in_neigh))


def direct_entry_neighbors(neighbors: Dict[str,Dict[str,str]], goal: str, current: Tuple[str,str], score: int):
    # print('  2nd',goal,current,score)
    if current[0] == goal:
        # the act of pressing A
        # print('  2nd',current,('pushed','A'),1,score+1)
        yield (score+1,('P','A'))
    else:
        for neigh,in_neigh in neighbors[current[0]].items():
            # the act of pressing a single arrow key
            # print('  2nd',current,(neigh,in_neigh),1,score+1)
            yield (score+1,(neigh,in_neigh))



total_score = 0

with open('Day21/input.txt') as f:
    for line in f:
        sequence = line.strip()
        sequence_value = int(sequence[:-1])
        sequence_length = 0
        current = 'A'
        for ch in sequence:
            result = breadth_first_search((current,'A'), is_pushed, partial(indirect_entry_neighbors,partial(indirect_entry_neighbors,partial(direct_entry_neighbors,arrow_neighbors_dict),arrow_neighbors_dict),numpad_neighbors_dict,ch))
            if result is None:
                print(f'no path found from {current} to {ch}???')
                exit(1)
            
            sequence_length += result
            current = ch


        total_score += sequence_length * sequence_value

print('Part 1:',total_score)
