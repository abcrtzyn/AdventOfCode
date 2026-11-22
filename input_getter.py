# Input getter script
# this script gets a full year of inputs
# Use case:
# You download the repo for the first time, and you have to fill in the inputs
# set your session cookie variable
# set your user agent string
# then run the program with the year as an argument


from datetime import date
import os
import sys

import time
import urllib.request
import urllib.error


SESSION_COOKIE = os.getenv("AOC_SESSION")
if SESSION_COOKIE is None:
    print('Please set your session cookie by running "export AOC_SESSION="session cookie string"')
    exit(1)

USER_AGENT = os.getenv("USER_AGENT")
if USER_AGENT is None:
    print('Please set your user agent string by running "export USER_AGENT="something that identifies you"')

if len(sys.argv) != 2:
    print('expected one argument [year]')
    exit(1)

year = int(sys.argv[1])

if not (2015 <= year <= date.today().year):
    print(f'not a valid year, should be between 2015 and {date.today().year}')


for day in range(1, 26):
    folder = f"year{year}/day{day:02d}"
    filepath = f"{folder}/input.txt"

    if os.path.exists(filepath):
        # skip if the file exists
        print(f'Day {day}, skipping, file exists')
        continue

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    req = urllib.request.Request(url, headers={"Cookie": f"session={SESSION_COOKIE}", "User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            with open(filepath, 'w') as f:
                f.write(data)
            print(f'Day {day}, success')
    except urllib.error.HTTPError as e:
        print(f'Day {day}, failed')
        raise e

    time.sleep(1.5)

