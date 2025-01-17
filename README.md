# My solutions to Advent of Code

So far, I have completed 2015, 2016, 2017, 2023, 2024, and over half of 2018 and 2021.
My first Advent of Code was 2021 and have since worked backwards and forwards.

Advent of Code has been an excellent learning oppurtunity for learning about different types of problems, data structures, languages, and different styles of programming.

I have learned APL from doing these challenges, and have become a huge fan of array based programming. It has changed how I think about problems. It may be evident in some of my Python solutions. Several of my Python solutions now use itertools functions and mapping over iterators because that is what an array based solution would do.

Advent of Code is mainly about solving problems. Although, programming is usually necessary to solve the problem, it takes some thinking to find an efficient solution. Occasionally there will not be any code, or there will be code that has nothing to with the input because I have done some work by hand to better understand the problem.

An example of this is the assembly puzzles. In some instances, rather than writing an interpreter to run the assembly code, I will work through it by hand to see what it does. I try and leave some notes about what my thought process is.

I first try to quickly find a solution, but then will go back through and make solutions better.

### Status

'status.csv' describes the status of each problem.

- Stars shows how many parts are completed
- Status shows what work there is left
    - 'done' indicates that solutions are complete. I may try to solve them using a different method later.
    - 'work' indicates that it is to be worked into a standardized form, simplified, and or made clearer
    - 'rework' means there is a solution that the solution I use to solve it is not there. I essentially have to resolve it
    - 'solve' means that there are still unsolved parts

It also marks which languages are used in each day.

### Todo

'todo.txt' is a list of items that I would like to get around to doing, usually solving in a different language.

### Running files

Not all files are standard. As I work through solutions again, I will standardize them to the following.

- Programs assume they are run from inside the year folder, meaning move into 2023 and run ```python3 Day06/main.py``` finding their input at 'Day06/input.txt'
- Python scripts are run from a virtual python environment in the base folder.
- Dyalog scripts are run using ```dyalogscript Day01/apl.apl```
- Haskell programs are compiled using ```ghc``` and run as a program
