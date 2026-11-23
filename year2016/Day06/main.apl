⎕FIX 'file://../apl_utils/utils.apln'

input ← Utils.readLines 'Day06/input.txt'

⍝ the bulk of this solution comes from APLCart sorted frequency table

⍝ part 1
⎕←'Part 1: ', ({1⊃⍵⌷⍨⊃⍒⊢/⍵}{⍺,≢⍵}⌸)¨↓⍉↑ input
                                    ⍝ get each column
                                   ⍝ for each
                            ⍝ frequency table
                      ⍝ sort the table
                     ⍝ get the first one
                ⍝ get only the letter 

⍝ part 2, sort the other way
⎕←'Part 2: ', ({1⊃⍵⌷⍨⊃⍋⊢/⍵}{⍺,≢⍵}⌸)¨↓⍉↑ input
