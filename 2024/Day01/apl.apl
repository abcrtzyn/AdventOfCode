parsed ← ↓⍉↑⍎¨⊃⎕NGET'Day01/test_input.txt' 1


⎕ ← 'Part 1: ' , +/|-⌿↑(⊂∘⍋⌷⊢)¨ parsed
                       ⍝ sort each list
                    ⍝


⎕ ← 'Part 2: ' , +/(⊃parsed[1])×+/(⊃ parsed[1]) ∘.= ⊃ parsed[2]
