R←⊃⎕NGET 'Day06/input.txt' 1

⍝ the bulk of this solution comes from APLCart sorted frequency table

⍝ part 1
⎕←'Part 1: ', ({1⊃⍵⌷⍨⊃⍒⊢/⍵}{⍺,≢⍵}⌸)¨↓⍉↑R
                                    ⍝ get each column
                                   ⍝ for each
                            ⍝ frequency table
                      ⍝ sort the table
                     ⍝ get the first one
                ⍝ get only the letter 

⍝ part 2, sort the other way
⎕←'Part 2: ', ({1⊃⍵⌷⍨⊃⍋⊢/⍵}{⍺,≢⍵}⌸)¨↓⍉↑R
