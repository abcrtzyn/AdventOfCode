]cd 'Documents/AdventOfCode/2022'

R←⊃⎕NGET 'Day02/input.txt' 1

oppSym←{↓('ABC'∘⍳1∘(↑[1]))↑⍵}
meSym←{↓('XYZ'∘⍳¯1∘(↑[1]))↑⍵}

⍝ part 1
+/{(1+meSym ⍵)+3×3|1+(meSym-oppSym)⍵} R

⍝ part 2, now meSym is lose draw win - 2 
+/{(3×meSym ⍵)+1+3|(2+meSym+oppSym)⍵} R