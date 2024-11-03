⎕IO ← 0 
R←⊃⎕NGET 'C:\Users\tater\Documents\AdventOfCode\2015\Day06\input.txt' 1
b←{⍺⍺='t':⍺≠⍵ ⋄ ⍺⍺='n':⍺∨⍵ ⋄ ⍺⍺='f':⍵∧~⍺}
instruction←{⍵⊃((∧⌿' ,'∘(∘.≠))⊆⊢)¨R}
nextGrid←{((((⍎1⊃⍺)∘≤∧(⍎3⊃⍺)∘≥)∘.∧((⍎2⊃⍺)∘≤∧(⍎4⊃⍺)∘≥))⍳1000)((⊃⍺)b)⍵}
⍝ left instruction, right grid
+/+/1⊃({(1∘+⊃⍵) ((instruction ⊃⍵) nextGrid 1⊃⍵)}⍣{299∘≤⊃⍵}) 0 (1000 1000 ⍴ 0) ⍝ part 1

c←{⍺⍺='t':⍵+2×⍺ ⋄ ⍺⍺='n':⍺+⍵ ⋄ ⍺⍺='f':0⌈⍵-⍺}
nextGrid2←{((((⍎1⊃⍺)∘≤∧(⍎3⊃⍺)∘≥)∘.∧((⍎2⊃⍺)∘≤∧(⍎4⊃⍺)∘≥))⍳1000)((⊃⍺)c)⍵}
+/+/1⊃({(1∘+⊃⍵) ((instruction ⊃⍵) nextGrid2 1⊃⍵)}⍣{10∘≤⊃⍵}) 0 (1000 1000 ⍴ 0) ⍝ part 2