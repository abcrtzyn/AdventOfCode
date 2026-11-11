⎕IO ← 0
R←⊃⎕NGET 'Day06/input.txt' 1

trans ← {
    ⍝ from APL Cart
    matches←⍵.(1↓Lengths↑¨Offsets↓¨⊂Block)
    ⍝ convert word to character
    c←'tfn'⌷⍨('toggle')('turn off')('turn on')⍳⊂0⊃matches
    ⍝ convert numbers and 
    c,⍎¨1↓matches
}
re ← '^(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)$'

parsed←(re ⎕S trans) R

⍝ I wonder if you can reduce using an asymmetric reduction like folding in haskell
⍝ turns out you can. Amazing



part1←{⍺⍺='t':⍺≠⍵ ⋄ ⍺⍺='n':⍺∨⍵ ⋄ ⍺⍺='f':⍵∧~⍺}

⍝ right argument is the grid
⍝ left argument is an instruction

nextGrid←{(⍺({(⍵≥1⊃⍺)∧⍵≤3⊃⍺}∘.∧{(⍵≥2⊃⍺)∧⍵≤4⊃⍺})⍳1000)((⊃⍺)part1)⍵}
                                                                ⍝ grid
          ⍝ a boolean mask cross product for the numbers
                                                       ⍝ apply the function for that letter

 
⎕←'Part 1: ', +/+/ ⊃ nextGrid/ (⌽ parsed) , ⊂ 1000 1000 ⍴ 0
                                                   ⍝ empty grid
                                    ⍝ prepend the instruction reversed
                    ⍝ fold the instructions
             ⍝ sum the lights

part2←{⍺⍺='t':⍵+2×⍺ ⋄ ⍺⍺='n':⍺+⍵ ⋄ ⍺⍺='f':0⌈⍵-⍺}
⍝ nextGrid is the same expect the new functions
nextGrid←{((((1⊃⍺)∘≤∧(3⊃⍺)∘≥)∘.∧((2⊃⍺)∘≤∧(4⊃⍺)∘≥))⍳1000)((⊃⍺)part2)⍵}

⎕←'Part 2: ', +/+/ ⊃ nextGrid/ (⌽ parsed) , ⊂ 1000 1000 ⍴ 0
