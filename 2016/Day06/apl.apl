R←⊃⎕NGET 'Day06/input.txt' 1

⍝ part 1
⊃¨({⍵⌷⍨⊂⍒⊢/⍵}{⍺,≢⍵}⌸)¨↓⍉↑R
⍝ part 2, sort the other way
⊃¨({⍵⌷⍨⊂⍋⊢/⍵}{⍺,≢⍵}⌸)¨↓⍉↑R
