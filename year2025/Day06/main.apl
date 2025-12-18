file ← ⊃⎕NGET 'Day06/input.txt' 1
⍝ partition each line by spaces
parse1 ← (' '∘≠⊆⊢)¨file

⍝ get just the operations and make them a simple array
ops ← ⊃¨⊃ ⌽ parse1

numbers1 ← ↓ ⍉ ↑ ⍎¨¨ ¯1 ↓ parse1
                     ⍝ drop the operations
                 ⍝ parse the numbers
           ⍝ transpose

⍝ if the op is +, plus reduce, if *, times reduce
apply ← {
    ⍺='+': +/⍵
    ⍺='*': ×/⍵
}

⎕PP ← 18
⎕←'Part 1: ', +/ ops apply¨ numbers1

numbers2 ← ⍎¨¨((∨/∊∘⎕D)¨⊆⊢) ↓ ⍉ ↑ ¯1 ↓ file
                                  ⍝ drop the ops
                            ⍝ transpose the columns into rows
              ⍝ partition by has digit (if it doesn't have a digit, than its a gap between problems)
            ⍝ turn them into numbers

⍝ do the exact same as part 1, same ops too.
⎕←'Part 2: ', +/ ops apply¨ numbers2



