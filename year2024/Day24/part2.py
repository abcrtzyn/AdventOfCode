# every half adder has an XOR and an AND gate, lets find these


from typing import Tuple, List, Dict


xors: List[Tuple[str,str]] = []
ands: Dict[str,str] = {}
ors: List[Tuple[str,str]] = []

with open('Day24/input.txt') as f:
    mode = 0
    for line in f:
        line = line.strip()
        if line == '':
            mode += 1
            continue
    
        if mode == 1:
            exp, name = line.split(' -> ')
            _, op, _ = exp.split(' ')
            if op == 'XOR':
                xors.append((exp,name))
            elif op == 'AND':
                ands[exp] = name
            elif op == 'OR':
                ors.append((exp,name))


first_layer_half_adders = []
second_layer_half_adders = []

# for each xor, find the and
for exp,xor_out in xors:
    a1, _, a2 = exp.split(' ')
    # find the corresponding and
    
    if f'{a1} AND {a2}' in ands:
        and_out = ands[f'{a1} AND {a2}']
    elif f'{a2} AND {a1}' in ands:
        and_out = ands[f'{a2} AND {a1}']
    else:
        print('couldn\'t find an and')
        exit(1)
    
    if a1[1:].isnumeric():
        first_layer_half_adders.append((a1,a2,xor_out,and_out))
    else:
        second_layer_half_adders.append((a1,a2,xor_out,and_out))

first_layer_half_adders_by_and_res = {d:(a,b,c,d) for a,b,c,d in first_layer_half_adders}
second_layer_half_adders_by_and_res = {d:(a,b,c,d) for a,b,c,d in second_layer_half_adders}

full_adders = [] 
# each OR matches up half adders
# there should be one of them in first layer and second layer
for exp,or_out in ors:
    a1, _, a2 = exp.split(' ')

    half_adder1 = None
    half_adder2 = None

    if a1 in first_layer_half_adders_by_and_res:
        half_adder1 = first_layer_half_adders_by_and_res[a1]
        del first_layer_half_adders_by_and_res[a1]
        if a2 in second_layer_half_adders_by_and_res:
            half_adder2 = second_layer_half_adders_by_and_res[a2]
            del second_layer_half_adders_by_and_res[a2]
    elif a1 in second_layer_half_adders_by_and_res:
        half_adder2 = second_layer_half_adders_by_and_res[a1]
        del second_layer_half_adders_by_and_res[a1]
        if a2 in first_layer_half_adders_by_and_res:
            half_adder1 = first_layer_half_adders_by_and_res[a2]
            del first_layer_half_adders_by_and_res[a2]
    elif a2 in first_layer_half_adders_by_and_res:
        half_adder1 = first_layer_half_adders_by_and_res[a2]
        del first_layer_half_adders_by_and_res[a2]
    elif a2 in second_layer_half_adders_by_and_res:
        half_adder2 = second_layer_half_adders_by_and_res[a2]
        del second_layer_half_adders_by_and_res[a2]

    full_adders.append((half_adder1,half_adder2,exp,or_out))

for x in full_adders:
    print(x)
for x in first_layer_half_adders_by_and_res.values():
    print(x)
for x in second_layer_half_adders_by_and_res.values():
    print(x)
