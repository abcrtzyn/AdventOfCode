# this script makes a new directory with the year
# and then adds 25 directories for days 1 through 25

YEAR = 2025

import os

os.mkdir(f'year{YEAR}')
os.chdir(f'year{YEAR}')
if YEAR <= 2024:
    max_day = 25
else:
    max_day = 12

for i in range(1,max_day+1):
    # print(f'Day{i:02d}')
    os.mkdir(f'Day{i:02d}')
