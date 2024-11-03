# assuming the input goes in order, this can be done as a recursive call

# looking for the directory whose size is minimum greater than 25623268

from io import TextIOWrapper


def trace(f: TextIOWrapper):
    size = 0;
    outputSize = 44376732;
    # expect ls command
    assert f.readline() == "$ ls\n","not ls";
    while True:
        tokens = f.readline().split();
        if(len(tokens) == 0):
            print(size)
            if(size >= 4376732 and outputSize > size):
                outputSize = size;
            print(outputSize);
            return (size, outputSize);
        if(tokens[0] == "$"):
            assert tokens[1] == "cd"
            if(tokens[2] == ".."):
                # TODO ending stuff
                print(size)
                if(size >= 4376732 and outputSize > size):
                    outputSize = size;
                print(outputSize);
                return (size, outputSize);
            else:
                ret = trace(f);
                size += ret[0];
                if(outputSize > ret[1]):
                    outputSize = ret[1];
        elif(tokens[0] == "dir"):
            pass
        else:
            # number
            size += int(tokens[0]);



with open("input.txt") as f:
    f.readline();
    rootSize = trace(f);
    print("Done", rootSize);