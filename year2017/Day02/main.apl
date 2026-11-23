⎕FIX 'file://../apl_utils/utils.apln'

⍝ parse numbers seperated by tabs from each line in file
input ← (⎕UCS 9)∘Utils.parseNumbers¨ Utils.readLines 'Day02/input.txt'

⍝ part 1
⎕ ← 'Part 1: ', +/(⌈/-⌊/)¨ input
                         ⍝ for each row
                      ⍝ min of the row
                   ⍝ max of the row
                     ⍝ difference
                ⍝ sum


⍝ part 2
⍝ create an identity matrix the same size as the left argument
ident←(⌽⍤⍴⍴1↑⍨1+≢)


⎕ ← 'Part 2: ', +/(÷/((⍸(∘.> ∧ 0=∘.(|⍨))⍨)⍛⌷))¨ input
                                              ⍝ for each row
                                   ⍝ mod (commuted)
                       ⍝(              ) this whole section is an outer product for > than and mod = 0
                                        ⍝ and the selfie to make it happen
                       ⍝ get the indicies of the single winner
                                           ⍝ get the values for that
                   ⍝ divide the two values
                ⍝ sum the rows results 

⍝ another version with a single outer product
⍝ this one is surely more readable
⍝ ⎕ ← 'Part 2: ', +/(÷/((⍸∘.(>∧ 0=|⍨)⍨)⍛⌷))¨ input
                           ⍝ single outer product here
