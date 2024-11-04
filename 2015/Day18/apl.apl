R ← ⊃ ⎕NGET 'Day18/input.txt' 1

A←'#'=↑R ⍝ convert to 1s and 0s and into matrix

iter←(({+/+/⍵}⌺3 3){(3=⍺)∨(⍵)∧(4=⍺)}⊢) ⍝ iterate once

⍝ part 1
+/+/((({+/+/⍵}⌺3 3){(3=⍺)∨(⍵)∧(4=⍺)}⊢)⍣100) A

corners←(26@(1 0 1 0 1 0 1 0⊂0 0 99 0 0 99 99 99))100 100 ⍴ 0

⍝ part 2
+/+/((({+/+/⍵}⌺3 3){corners∨(3=⍺)∨(⍵)∧(4=⍺)}⊢)⍣100) A
