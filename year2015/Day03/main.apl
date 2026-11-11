R←⊃⊃⎕NGET 'Day03/input.txt' 1

⍝ convert the text into directions
parsed ← ((1 0) (0 1) (¯1 0) (0 ¯1))['>^<v'⍳R]



⎕←'Part 1: ', ≢∪ (0 0)⍪ +⍀ ↑ parsed
                           ⍝ convert to table
                        ⍝ plus scan the columns
                 ⍝ include the starting point
              ⍝ count uniques (at least one present) 

⎕←'Part 2: ', ≢∪ (0 0)⍪ {((≢⍵) 2)⍴+⍀((2÷⍨≢⍵) 4)⍴⍵} ↑ parsed
                                                   ⍝ convert to table
                                     ⍝ convert to 4 columns (split input every other)
                                  ⍝ plus scan columns
                         ⍝ convert back to 2 columns
                 ⍝ include the starting point
             ⍝ count uniques
