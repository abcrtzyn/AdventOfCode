

terms_original = {}

#  parsing the terms
with open('Day07/input.txt') as f:
    for line in f.readlines():
        expression, name = [x.strip() for x in line.strip().split(' -> ')]
        if expression.isnumeric():
            terms_original[name] = int(expression)
        else:
            terms_original[name] = expression

# calculates the name given using term bank
# calculates all dependicies and simplifies them in the bank
# returns the integer result of the computation
def calculate(name,terms):
    if name.isnumeric():
        # if it is a numeric string (usually second argument of a shift)
        # return the int
        return int(name)
    # otherwise, get the expression
    expression = terms[name]
    
    if type(expression) == int:
        # if the expression is already an int, return that
        return expression
    else:
        # string
        expression = expression.split()
        if len(expression) == 1:
            # direct input (a -> b)
            ans = calculate(expression[0],terms)
            terms[name] = ans
            return ans
        elif len(expression) == 2:
            if expression[0] == 'NOT':
                ans = ~ calculate(expression[1],terms)
                terms[name] = ans
                return ans
        elif len(expression) == 3:
            if expression[1] == 'OR':
                ans = calculate(expression[0], terms) | calculate(expression[2], terms)
                terms[name] = ans
                return ans
            elif expression[1] == 'AND':
                ans = calculate(expression[0], terms) & calculate(expression[2],terms)
                terms[name] = ans
                return ans
            elif expression[1] == 'LSHIFT':
                ans = calculate(expression[0],terms) << calculate(expression[2],terms)
                terms[name] = ans
                return ans
            elif expression[1] == 'RSHIFT':
                ans = calculate(expression[0],terms) >> calculate(expression[2],terms)
                terms[name] = ans
                return ans
                

    raise Exception('unknown expression',expression)


terms1 = terms_original.copy()

part1 = calculate('a',terms1)
print('Part 1:', part1)

terms2 = terms_original.copy()
# override term b
terms2['b'] = part1
print('Part 2:', calculate('a',terms2))
