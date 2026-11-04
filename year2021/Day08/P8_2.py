from typing import List

import numpy as np

letters = "abcdefg"
summ = 0
with open('input.txt') as f:
    easyDigitsTotal = 0
    for line in f:
        combos: str
        combos, output = tuple([l.strip() for l in line.strip().split('|')])
        combosDigits = combos.split()
        gridl: List[List[int]] = []
        for i, combo in zip(range(0,10), combosDigits):
            gridl.append([])
            for j, l in zip(range(0,7),letters):
                gridl[i].append(l in combo)
        grid = np.array(gridl)
        digits = np.ndarray(grid.shape,dtype=np.bool8) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType, reportAttributeAccessIssue]
        
        segments = grid.sum(1)
        counts = grid.sum(0)
        digits[1] = grid[segments == 2][0]
        digits[7] = grid[segments == 3][0]
        digits[4] = grid[segments == 4][0]
        digits[8] = grid[segments == 7][0]
        
        segmentA = np.logical_and(digits[7], ~(digits[1]))
        segmentB = counts == 6
        segmentE = counts == 4
        segmentF = counts == 9
        segmentG = np.logical_not(np.logical_or.reduce((segmentA, digits[4], segmentE)))
        segmentC = np.logical_and(counts == 8, ~segmentA)
        segmentD = np.logical_and(counts == 7, ~segmentG)
        
        digits[0] = np.logical_or.reduce((segmentA, segmentB, segmentC, segmentE, segmentF, segmentG))
        digits[2] = np.logical_or.reduce((segmentA, segmentC, segmentD, segmentE, segmentG))
        digits[3] = np.logical_or.reduce((segmentA, segmentC, segmentD, segmentF, segmentG))
        digits[5] = np.logical_or.reduce((segmentA, segmentB, segmentD, segmentF, segmentG))
        digits[6] = np.logical_or.reduce((segmentA, segmentB, segmentD, segmentE, segmentF, segmentG))
        digits[9] = np.logical_or.reduce((segmentA, segmentB, segmentC, segmentD, segmentF, segmentG))

        outputDigits = output.split()
        outputGridl: List[List[int]] = []
        for i, output in zip(range(0,10), outputDigits):
            outputGridl.append([])
            for j, l in zip(range(0,7),letters):
                outputGridl[i].append(l in output)
        outputGrid = np.array(outputGridl)
        number = 0
        for n in outputGrid:
            number *= 10
            number += np.where((digits == n).all(axis=1))[0]
        print(number[0])
        summ += number[0]
    print(summ)
