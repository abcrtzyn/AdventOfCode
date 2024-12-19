# I suspect that there will be a cycle eventually

import numpy as np


# parse
with open('Day18/test_input.txt') as f:
    grid = np.array([[(0 if c=='.' else (1 if c=='|' else (2 if c=='#' else -1))) for c in line.strip()] for line in f],np.uint8)
    
# for grid in 
