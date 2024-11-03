]cd 'Documents/AdventOfCode/2022'

R←⊃⊃⎕NGET 'Day06/input.txt' 1

⍝ part 1
4+⊃⍸4=1↓({≢∪⍵}⌺4)R

⍝ part 2
14+⊃⍸14=6↓({≢∪⍵}⌺14)R