R←⊃⎕NGET (path,'\input_test.txt') 1
first←⊃R
insertions←2↓R
f←{(¯1↑⍵),⍨⊃,/(⊂↑(2↑¨⍺)⍳2,/⍵)∘⌷((⊂1 7)∘⌷¨⍺)}
insertions (f⍣1) first ⍝ apply 1 times
{⍺, ≢⍵}⌸ ⍝ count letters
(⌈/-⌊/) 2⊃↓[1] ⍝ subtract min from max
⍝ full thing all together
R←⊃⎕NGET (path,'\input_test.txt') 1
first←⊃R
insertions←2↓R
f←{(¯1↑⍵),⍨⊃,/(⊂↑(2↑¨⍺)⍳2,/⍵)∘⌷((⊂1 7)∘⌷¨⍺)}
(⌈/-⌊/) 2⊃↓[1] {⍺, ≢⍵}⌸ insertions (f⍣10) first

