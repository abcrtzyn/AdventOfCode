
R ← ⊃⊃ ⎕NGET 'Day12/input.txt' 1

⍝ part 1
⎕ ← 'Part 1: ', +/⍎¨({∨⌿('-',⎕D)∘.=⍵}⊆⊢) R

⍝ I would like to make an efficient way of parsing a JSON to get the values without red
