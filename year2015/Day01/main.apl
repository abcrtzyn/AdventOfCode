⎕FIX 'file://../apl_utils/utils.apln'

input ← Utils.readSingleLine 'Day01/input.txt'

⍝ old solution
⍝ ('('∘=-⍥(+/)')'∘=)R
⎕←'Part 1: ', -⌿+/'()'∘.= input
⍝ difference between the number of open parens and close parens


⎕←'Part 2: ', ⊃⍸¯1=+\1-⍨2×'('∘= input
                     ⍝ this is one way to get 1 for open, -1 for close
                   ⍝ plus scan, this is the floors visited after each character
              ⍝ find the first that is ¯1

⍝ for part 2, you could similarly do part 1 for each prefix string of the file
