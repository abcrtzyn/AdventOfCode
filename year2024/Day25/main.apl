
parsed←↑¨((''∘≢¨⊢)⊆⊢)⊃⎕NGET 'Day25/input.txt' 1
           ⍝ partion by double line break
       ⍝ make each into a grid

locks←(('#'=(⊂1 1)⌷¨⊢)⊢⍤/⊢)parsed
keys←(('#'≠(⊂1 1)⌷¨⊢)⊢⍤/⊢)parsed
⍝ split locks and keys, filtering by the upper left corner


⍝ in the following outer product, keys are matched with locks
⍝ any cells in each grid that both have a # mark overlap
part1 ← +/+/~ locks∘.{∨/∨/('#'=⍵)∧('#'=⍺)}keys
                   ⍝ outer product
                           ⍝ for each grid cell
                           ⍝ if both lock and key have # in that spot, it is a 1
                     ⍝ reduce to 1 if overlap, 0 if no overlap
            ⍝ negate
        ⍝ count all nonoverlapping lock/key pairs

⎕ ← 'Part 1:', part1
