]CD 'Documents/AdventOfCode/2015'
R ← ⊃ ⎕NGET 'Day12/input.txt' 1

⍝ part 1
+/⍎¨({∨⌿('-',⎕D)∘.=⍵}⊆⊢)⊃R