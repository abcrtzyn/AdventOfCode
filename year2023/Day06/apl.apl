⍝ manual input this data

⍝ test data
⍝ records ← (7 9) (15 40) (30 200)
⍝ my data
records ← (48 255) (87 1288) (69 1117) (81 1623)

⍝ this method tries each possible i
⎕←'Part 1: ',×/{+/(2⊃⍵)<(⊢{(⍺×⍵)-(⍵×⍵)}⍳)⊃⍵}¨records
