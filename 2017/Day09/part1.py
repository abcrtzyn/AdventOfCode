from io import TextIOWrapper


def handle_group(stream: TextIOWrapper, score = 1):
    # already read the first char
    # the structure of the rest is comma seperated garbage or groups
    total_score = score
    total_garbage = 0

    while True:
        # expecting { < }
        c = stream.read(1)
        match c:
            case '}':
                # group done
                return (total_score,total_garbage)
            case '{':
                # start another group
                add_score, add_garbage = handle_group(stream, score+1) # returns when closed
                total_score += add_score
                total_garbage += add_garbage
            case '<':
                # start garbage
                total_garbage += handle_garbage(stream)
            case _:
                print(f'group first {c}')
                exit(1)
        
        # after group or garbage
        # expect , or }
        c = stream.read(1)
        match c:
            case '}':
                # group done
                return (total_score,total_garbage)
            case ',':
                pass
            case _:
                print(f'group second {c}')
                exit(1)



def handle_garbage(stream: TextIOWrapper):
    total_garbage = 0
    while True:
        c = stream.read(1)
        match c:
            case '>':
                # garbage done
                return total_garbage
            case '!':
                # ignore the next thing
                stream.read(1)
            case _:
                total_garbage += 1
                pass
        




with open('Day09/input.txt') as f:
    c = f.read(1)
    if c == '{':
        print(handle_group(f))
    else:
        print('what input file do you have that doesn\'t start with a open curly brace?')
        exit(1)
