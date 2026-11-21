parsed ← ↓⍉↑⍎¨⊃⎕NGET'Day01/input.txt' 1


⎕ ← 'Part 1: ' , +/|-⌿↑(⊂∘⍋⌷⊢)¨ parsed
                       ⍝ sort each list
                    ⍝ take differences
                 ⍝ sum differences


⎕ ← 'Part 2: ' , +/(⊃parsed[1])×+/(⊃ parsed[1]) ∘.= ⊃ parsed[2]
                                                ⍝ find all equals
                                ⍝ sum occurances
                     ⍝ multiply by the values
                 ⍝ sum
