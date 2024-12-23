from collections import deque

# gives the next price in the sequence, 2001 times, including the initial
def market_price(seed: int):
    yield seed % 10
    for _ in range(2000):
        seed = (seed ^ (seed << 6)) & 0xFFFFFF
        seed = (seed ^ (seed >> 5))
        seed = (seed ^ (seed << 11)) & 0xFFFFFF
        yield seed % 10

# generates the sequence of 4 market changes
# yields ((4 number sequence), price)
def market_changes(seed: int):
    prices = market_price(seed)
    
    # using a deque of maxlen 4 means it will only ever keep 4 values
    # its quite a flexible data structure
    changes = deque([],4)
    
    # a stores the last price, b stores the current price
    price = 0
    last_price = 0

    # this loop creates the sequences that are too short
    for _ in range(4):
        price = next(prices)
        changes.append(price-last_price)
        # shift prices
        last_price = price

    # and now for the rest
    for price in prices:
        changes.append(price-last_price)
        yield (tuple(changes),price)
        # shift prices
        last_price = price


# keeps track of all the sequences and what the total number of bananas recieved for it
sequences_master = {}


with open('Day22/input.txt') as f:
    # for each buyer
    for line in f:
        # make a list of all the sequences and their costs
        sequences = {}

        changes = market_changes(int(line))
        for seq,price in changes:
            if seq in sequences:
                # if the sequence already occured, do not record it
                continue
            # record it
            sequences[seq] = price

        # offload sequences into master
        for seq, price in sequences.items():
            if seq in sequences_master:
                sequences_master[seq] += price
            else:
                sequences_master[seq] = price
        
# find the max value
print('Part 2:',max(sequences_master.values()))
# doesn't matter what the sequence is, but this max function will find it
# m = max(sequences_master,key=sequences_master.get)  # type: ignore
