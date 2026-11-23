⎕FIX 'file://../apl_utils/utils.apln'

input ← Utils.readSingleLine 'Day03/input.txt'

⍝ convert the text into directions
parsed ← ↑ ((1 0) (0 1) (¯1 0) (0 ¯1))['>^<v'⍳input]



⎕←'Part 1: ', ≢∪ (0 0)⍪ +⍀ parsed
                        ⍝ plus scan the columns
                 ⍝ include the starting point
              ⍝ count uniques (at least one present) 

⎕←'Part 2: ', ≢∪ (0 0)⍪ {((≢⍵) 2)⍴+⍀((2÷⍨≢⍵) 4)⍴⍵} parsed
                                     ⍝ convert to 4 columns (split input every other)
                                  ⍝ plus scan columns
                         ⍝ convert back to 2 columns
                 ⍝ include the starting point
             ⍝ count uniques
