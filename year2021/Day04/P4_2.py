import numpy as np

with open('input.txt','r') as f:
    # a list of the bingo call numbers
    callNumbers = [int(n) for n in f.readline().strip().split(',')]
    f.readline()
    numbers = [line.strip().split() for line in f.readlines()]


numbers = [line for i, line in enumerate(numbers) if i % 6 != 5]
boards = np.array(numbers).astype(np.int8).reshape((len(numbers)//5,5,5))
covered = np.zeros((len(numbers)//5,5,5), dtype=np.bool8)

for n in callNumbers:
    covered: np.ndarray = np.logical_or(covered, boards == n)
    hasBingo: np.ndarray = np.logical_or(np.any(covered.sum(1) == 5 ,1), np.any(covered.sum(2) == 5, 1))
    if np.all(hasBingo):
        lastBingo = np.logical_xor(lastHasBingo, hasBingo)
        if lastBingo.sum() > 1:
            print("too many last bingos")
            break
        print(n * (boards[lastBingo][0][np.logical_not(covered[lastBingo][0])]).sum())
        break
    lastHasBingo = hasBingo