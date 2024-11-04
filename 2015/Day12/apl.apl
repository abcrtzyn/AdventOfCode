
R ← ⊃ ⎕NGET 'Day12/input.txt' 1

⍝ part 1
+/⍎¨({∨⌿('-',⎕D)∘.=⍵}⊆⊢)⊃R
