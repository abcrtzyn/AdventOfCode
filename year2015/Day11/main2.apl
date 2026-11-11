⍝ this solution I'm building in the ILO rule
⍝ in order to just immediately skip over them

input ← ⊃⊃ ⎕NGET 'Day11/input.txt' 1

stringtodigits ← {0 1 2 3 4 5 6 7 8 8 9 10 10 11 12 12 13 14 15 16 17 18 19 20 21 22[(¯1 ⎕C ⎕A)⍳⍵]}
digitstostring ← {'abcdefghjkmnpqrstuvwxyz'[1+⍵]}

digitstonumber ← 23∘⊥
numbertodigits ← (8⍴23)∘⊤

inputnumber ← digitstonumber stringtodigits input

⍝ has 'abc' 'bcd'
hasstep ← 1∊2∧/((¯1↓(∧⌿7 9 11∘.≠⊢))∧(2(1=-)⍨/⊢))
                                    ⍝ difference between two chars is 1
                ⍝ and it isnt one of the ilo skips
             ⍝ there are two of them in a row
          ⍝ any true

⍝ has two pairs that are different
hastwopair ← {2≤≢∪(0,2=/⍵)/⍵}
                    ⍝ make mask of pairs
                          ⍝ get the numbers for those pairs
              ⍝ are there at least two different numbers



isvalid←{(hastwopair ∧ hasstep) numbertodigits ⍺}

⍝ The power function essentially a while loop
⍝ increment i and test the value
part1 ← (1∘+⍣isvalid) inputnumber
⎕ ← 'Part 1: ', digitstostring numbertodigits part1
part2 ← (1∘+⍣isvalid) part1
⎕ ← 'Part 2: ', digitstostring numbertodigits part2
