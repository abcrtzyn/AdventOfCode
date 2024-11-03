# assuming the input goes in order, this can be done as a recursive call


from io import TextIOWrapper


def trace(f: TextIOWrapper):
    size = 0;
    outputSize = 0;
    # expect ls command
    assert f.readline() == "$ ls\n","not ls";
    while True:
        tokens = f.readline().split();
        if(len(tokens) == 0):
            if(size <= 100000):
                outputSize += size;
            return (size, outputSize);
        if(tokens[0] == "$"):
            assert tokens[1] == "cd"
            if(tokens[2] == ".."):
                # TODO ending stuff
                if(size <= 100000):
                    outputSize += size;
                return (size, outputSize);
            else:
                ret = trace(f);
                size += ret[0];
                outputSize += ret[1];
        elif(tokens[0] == "dir"):
            pass
        else:
            # number
            size += int(tokens[0]);



with open("input.txt") as f:
    f.readline();
    rootSize = trace(f);
    print("Done", rootSize);