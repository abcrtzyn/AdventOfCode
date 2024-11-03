# %%
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

replacements = dict()

# %%
with open('input_test.txt') as f:
    inputString = f.readline().strip()
    f.readline()
    for line in f:
        # create all the replacement string
        key, insert = tuple(line.strip().split(' -> '))
        replace = key[0] + insert
        replacements[key] = replace
# %%
string = np.array(list(inputString))
# %%


#NNCB
#NN NC CB B
#NC NB CH B
#NCNBCHB
