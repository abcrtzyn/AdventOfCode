]CD 'Documents/AdventOfCode/2015'
R ← ⊃ ⎕NGET 'Day16/input.txt' 1
keys ← 'children' 'cats' 'samoyeds' 'pomeranians' 'akitas' 'vizslas' 'goldfish' 'trees' 'cars' 'perfumes'

({((2÷⍨⍴⍵),2)⍴⍵}({∧⌿':, '∘.≠⍵}⊆⊢))¨(((1∘+' '∘(⍳⍨))↓⊢)4∘↓)¨3↑R