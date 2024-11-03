terms = {}

with open('Day07/inputpart2.txt') as f:
    for line in f.readlines():
        eq, term = [x.strip() for x in line.strip().split(' -> ')]
        if eq.isnumeric():
            terms[term] = int(eq)
        else:
            terms[term] = eq

def calculate(term):
    if term.isnumeric():
        return int(term)
    eq = terms[term]
    #print('current', term, '=', eq)
    if type(eq) == int:
        return eq
    else:
        # string
        eq = eq.split()
        if len(eq) == 1:
            # direct input
            ans = calculate(eq[0])
            #print(term,'=',ans)
            terms[term] = ans
            return ans
        elif len(eq) == 2:
            if eq[0] == 'NOT':
                ans = ~ calculate(eq[1])
                #print(term,'=',ans)
                terms[term] = ans
                return ans
        elif len(eq) == 3:
            if len(eq) == 3:
                if eq[1] == 'OR':
                    ans = calculate(eq[0]) | calculate(eq[2])
                    #print(term,'=',ans)
                    terms[term] = ans
                    return ans
                elif eq[1] == 'AND':
                    ans = calculate(eq[0]) & calculate(eq[2])
                    #print(term,'=',ans)
                    terms[term] = ans
                    return ans
                elif eq[1] == 'LSHIFT':
                    ans = calculate(eq[0]) << calculate(eq[2])
                    #print(term,'=',ans)
                    terms[term] = ans
                    return ans
                elif eq[1] == 'RSHIFT':
                    ans = calculate(eq[0]) >> calculate(eq[2])
                    #print(term,'=',ans)
                    terms[term] = ans
                    return ans
                

    raise Exception(eq)


print(calculate('a'))
