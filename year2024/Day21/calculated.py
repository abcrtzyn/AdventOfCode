# left before down/up before right
# except for when left is impossible
# or when up/down is impossible
paths_lookup = {
    ('0', '0') :'A',
    ('0', '1') :'^<A',   # EXCEPTION up before left
    ('0', '2') :'^A',
    ('0', '3') :'^>A',
    ('0', '4') :'^^<A',  # EXCEPTION up before left
    ('0', '5') :'^^A',
    ('0', '6') :'^^>A',
    ('0', '7') :'^^^<A', # EXCEPTION up before left
    ('0', '8') :'^^^A',
    ('0', '9') :'^^^>A',
    ('0', 'A') :'>A',
    ('1', '0') :'>vA',   # EXCEPTION right before down
    ('1', '1') :'A',
    ('1', '2') :'>A',
    ('1', '3') :'>>A',
    ('1', '4') :'^A',
    ('1', '5') :'^>A',
    ('1', '6') :'^>>A',
    ('1', '7') :'^^A',
    ('1', '8') :'^^>A',
    ('1', '9') :'^^>>A',
    ('1', 'A') :'>>vA',  # EXCEPTION right before down
    ('2', '0') :'vA',
    ('2', '1') :'<A',
    ('2', '2') :'A',
    ('2', '3') :'>A',
    ('2', '4') :'<^A',
    ('2', '5') :'^A',
    ('2', '6') :'^>A',
    ('2', '7') :'<^^A',
    ('2', '8') :'^^A',
    ('2', '9') :'^^>A',
    ('2', 'A') :'v>A',
    ('3', '0') :'<vA',
    ('3', '1') :'<<A',
    ('3', '2') :'<A',
    ('3', '3') :'A',
    ('3', '4') :'<<^A',
    ('3', '5') :'<^A',
    ('3', '6') :'^A',
    ('3', '7') :'<<^^A',
    ('3', '8') :'<^^A',
    ('3', '9') :'^^A',
    ('3', 'A') :'vA',
    ('4', '0') :'>vvA',  # EXCEPTION right before down
    ('4', '1') :'vA',
    ('4', '2') :'v>A',
    ('4', '3') :'v>>A',
    ('4', '4') :'A',
    ('4', '5') :'>A',
    ('4', '6') :'>>A',
    ('4', '7') :'^A',
    ('4', '8') :'^>A',
    ('4', '9') :'^>>A',
    ('4', 'A') :'>>vvA', # EXCEPTION right before down
    ('5', '0') :'vvA',
    ('5', '1') :'<vA',
    ('5', '2') :'vA',
    ('5', '3') :'v>A',
    ('5', '4') :'<A',
    ('5', '5') :'A',
    ('5', '6') :'>A',
    ('5', '7') :'<^A',
    ('5', '8') :'^A',
    ('5', '9') :'^>A',
    ('5', 'A') :'vv>A',
    ('6', '0') :'<vvA',
    ('6', '1') :'<<vA',
    ('6', '2') :'<vA',
    ('6', '3') :'vA',
    ('6', '4') :'<<A',
    ('6', '5') :'<A',
    ('6', '6') :'A',
    ('6', '7') :'<<^A',
    ('6', '8') :'<^A',
    ('6', '9') :'^A',
    ('6', 'A') :'vvA',
    ('7', '0') :'>vvvA', # EXCEPTION right before down
    ('7', '1') :'vvA',
    ('7', '2') :'vv>A',
    ('7', '3') :'vv>>A',
    ('7', '4') :'vA',
    ('7', '5') :'v>A',
    ('7', '6') :'v>>A',
    ('7', '7') :'A',
    ('7', '8') :'>A',
    ('7', '9') :'>>A',
    ('7', 'A') :'>>vvvA',# EXCEPTION right before down
    ('8', '0') :'vvvA',
    ('8', '1') :'<vvA',
    ('8', '2') :'vvA',
    ('8', '3') :'vv>A',
    ('8', '4') :'<vA',
    ('8', '5') :'vA',
    ('8', '6') :'v>A',
    ('8', '7') :'<A',
    ('8', '8') :'A',
    ('8', '9') :'>A',
    ('8', 'A') :'vvv>A',
    ('9', '0') :'<vvvA',
    ('9', '1') :'<<vvA',
    ('9', '2') :'<vvA',
    ('9', '3') :'vvA',
    ('9', '4') :'<<vA',
    ('9', '5') :'<vA',
    ('9', '6') :'vA',
    ('9', '7') :'<<A',
    ('9', '8') :'<A',
    ('9', '9') :'A',
    ('9', 'A') :'vvvA',
    ('A', '0') :'<A',
    ('A', '1') :'^<<A',  # EXCEPTION up before left
    ('A', '2') :'<^A',
    ('A', '3') :'^A',
    ('A', '4') :'^^<<A', # EXCEPTION up before left
    ('A', '5') :'<^^A',
    ('A', '6') :'^^A',
    ('A', '7') :'^^^<<A',# EXCEPTION up before left
    ('A', '8') :'<^^^A',
    ('A', '9') :'^^^A',
    # same for both keypads
    ('A', 'A') :'A',

    ('<', '<'): 'A',
    ('<', '^'): '>^A',   # EXCEPTION right before up
    ('<', '>'): '>>A',
    ('<', 'v'): '>A',
    ('<', 'A'): '>>^A',  # EXCEPTION right before up
    ('^', '<'): 'v<A',   # EXCEPTION down before left
    ('^', '^'): 'A',
    ('^', '>'): 'v>A',
    ('^', 'v'): 'vA',
    ('^', 'A'): '>A',
    ('>', '<'): '<<A',
    ('>', '^'): '<^A',
    ('>', '>'): 'A',
    ('>', 'v'): '<A',
    ('>', 'A'): '^A',
    ('v', '<'): '<A',
    ('v', '^'): '^A',
    ('v', '>'): '>A',
    ('v', 'v'): 'A',
    ('v', 'A'): '^>A',
    ('A', '<'): 'v<<A',  # EXCEPTION down before left
    ('A', '^'): '<A',
    ('A', '>'): 'vA',
    ('A', 'v'): '<vA',
}



from functools import cache


@cache
def calculate_sequence_length(seq: str, indirection: int) -> int:
    # starting at A, go to each in the sequence and press A
    if indirection == 0:
        return len(seq)
    
    length = 0

    char_a = 'A'
    for char_b in seq:
        path = paths_lookup[(char_a,char_b)]

        length += calculate_sequence_length(path,indirection-1)

        char_a = char_b
    
    return length


total_score1 = 0
total_score2 = 0

with open('Day21/input.txt') as f:
    for line in f:
        sequence = line.strip()
        l1 = calculate_sequence_length(sequence,3)
        total_score1 += l1 * int(sequence[:-1])
        
        l2 = calculate_sequence_length(sequence,26)
        total_score2 += l2 * int(sequence[:-1])

print('Part 1:',total_score1)
print('Part 2:',total_score2)
