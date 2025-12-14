


        ⍝ INPUT HERE
input ← 'hijklmmn'

stringtodigits ← (¯1+(¯1 ⎕C ⎕A)⍳⊢)
digitstostring ← {(¯1 ⎕C ⎕A)[1+⍵]}

digitstonumber ← 26∘⊥
numbertodigits ← (8⍴26)∘⊤

inputnumber ← digitstonumber stringtodigits input

⍝ has 'abc' 'bcd'
hasstep ← 1∊2∧/(2(1=-)⍨/⊢)
                  ⍝ difference between two chars is 1
             ⍝ there are two of them in a row
          ⍝ any true

⍝ has two pairs that are different
hastwopair ← {2≤≢∪(0,2=/⍵)/⍵}
                    ⍝ make mask of pairs
                          ⍝ get the numbers for those pairs
              ⍝ are there at least two different numbers

⍝ has any of the chars ILO
hasnotILO ← ~ 1 ∊ (8 11 14 ∊ ⊢)


isvalid←{{∧/(hastwopair ⍵) (hasnotILO ⍵) (hasstep ⍵)} numbertodigits ⍺}

⍝ The power function essentially a while loop
⍝ increment i and test the value
part1 ← (1∘+⍣isvalid) inputnumber
⎕ ← 'Part 1: ', digitstostring numbertodigits part1
part2 ← (1∘+⍣isvalid) part1
⎕ ← 'Part 2: ', digitstostring numbertodigits part2
