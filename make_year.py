# this script makes a new directory with the year
# and then adds 25 directories for days 1 through 25


YEAR = 2024

import os

os.mkdir(f'{YEAR}')
os.chdir(f'{YEAR}')
for i in range(1,26):
    # print(f'Day{i:02d}')
    os.mkdir(f'Day{i:02d}')
