⎕IO ← 0
R←⊃⎕NGET 'Day06/pro_input.txt' 1

parsed ← ((1↑[1]⊢),(⍎¨1↓[1]⊢))↑ ((~', '∘(∊⍨))⊆⊢)¨ R
                                                ⍝ for each line
                                             ⍝ partition
                                  ⍝ by commas and spaces
                              ⍝ into table
                    ⍝ parse the numbers
          ⍝ reattach the letters

⍝ I wonder if you can reduce using an asymmetric reduction like folding in haskell



part1←{⍺⍺='t':⍺≠⍵ ⋄ ⍺⍺='n':⍺∨⍵ ⋄ ⍺⍺='f':⍵∧~⍺}

⍝ right argument is the grid
⍝ left argument is an instruction
nextGrid←{((((1⊃⍺)∘≤∧(3⊃⍺)∘≥)∘.∧((2⊃⍺)∘≤∧(4⊃⍺)∘≥))⍳1000)((⊃⍺)part1)⍵}
                                                                   ⍝ grid
          ⍝ a boolean mask cross product for the numbers
                                                        ⍝ apply the function for that letter

 
⎕←'Part 1: ', +/+/ ⊃ nextGrid/ (⌽ ↓parsed) , ⊂ 1000 1000 ⍴ 0
                                                   ⍝ empty grid
                                    ⍝ prepend the instruction reversed
                    ⍝ fold the instructions
             ⍝ sum the lights

part2←{⍺⍺='t':⍵+2×⍺ ⋄ ⍺⍺='n':⍺+⍵ ⋄ ⍺⍺='f':0⌈⍵-⍺}
⍝ nextGrid is the same expect the new functions
nextGrid←{((((1⊃⍺)∘≤∧(3⊃⍺)∘≥)∘.∧((2⊃⍺)∘≤∧(4⊃⍺)∘≥))⍳1000)((⊃⍺)part2)⍵}

⎕←'Part 2: ', +/+/ ⊃ nextGrid/ (⌽ ↓parsed) , ⊂ 1000 1000 ⍴ 0
