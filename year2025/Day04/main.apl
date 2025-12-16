parsed ← ↑⊃⎕NGET 'Day04/input.txt' 1

⍝ love a nice clean solution. Stencil has to be the best operator

⍝ this creates a boolean grid of all the rolls that are accessible
part1 ← (⊢∧ 4≥({+/+/⍵}⌺3 3))
                       ⍝ split into 3 3 grids
                ⍝ sum the number of rolls around
            ⍝ if it is less than 4 + the center one
        ⍝ boolean and with if it is a roll or not


⎕ ← 'Part 1: ', +/+/ part1 '@'=parsed
                            ⍝ boolean roll
                ⍝ count it all


⍝ the power operator scares me a little
⍝ especially when using the fixpoint version
⍝ we will see what I can do

⍝ takes a grid of rolls and keeps are the rolls that are not accessible
part2 ← ((~ part1) ∧ ⊢)
                     ⍝ grid
          ⍝ not accessible
                  ⍝ boolean and


⎕←'Part 2: ', ((+/+/)-(+/+/∘(part2 ⍣≡))) '@'=parsed
                                         ⍝ boolean roll
                             ⍝ repeat the part2 fn until nothing changes
                             ⍝ leaving all rolls that can not move
                      ⍝ count the rest
               ⍝ compare that to the count of total rolls
              ⍝ left is the rolls removed
