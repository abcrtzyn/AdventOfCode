
R←⍎¨⊃⎕NGET 'Day02/input.txt' 1

⍝ part 1
⎕ ← 'Part 1: ', +/(⌈/-⌊/)¨R
                         ⍝ for each row
                      ⍝ min of the row
                   ⍝ max of the row
                   ⍝ difference
                ⍝ sum


⍝ part 2
⍝ create an identity matrix the same size as the left argument
ident←(⌽⍤⍴⍴1↑⍨1+≢)


⎕ ← 'Part 2: ', +/(÷/((⍸∘⍉((ident≠⊢)0=∘.|⍨))⌷⊢))¨R
                                                ⍝ for each row
                                       ⍝ take the mod of every pair
                                    ⍝ find the divisible pair
                           ⍝ not the diagonal 5/5=1
                        ⍝ transpose to get big/little
                       ⍝ get indicies
                                           ⍝ get those indicies
                  ⍝ divide reduce the two numbers
                ⍝ sum all rows
