parsed←⍎¨⊃⎕NGET'Day02/input.txt' 1

⍝ given a report, returns if it is safe
safe ← ({(∧/(3∘≥∧0∘≠)|⍵)∧((1=≢∘∪)×⍵)}2-/⊢)
                                     ⍝ take pairwise differences
                                 ⍝ signs
                          ⍝ are all the same, 1, -1, or 0
         ⍝ all differences are
         ⍝ non-zero, less than 3
       ⍝ conjuction all together

⎕ ← 'Part 1: ' , +/safe¨parsed

⍝ given a report, returns if it is safe with dampening
dampen ← {
    ⍝ check original case first
    safe ⍵: 1
    ⍝ then try remove elements
    ∨/ safe¨ (↓~(,⍨⍴1↑⍨1∘+)(≢⍵))/¨ (⊂⍵)
                 ⍝ create identity mat
               ⍝ negate
              ⍝ split rows
                                ⍝ remove single elements (see below)
    ⍝ at least one is safe 
}

⎕ ← 'Part 2: ' , +/ dampen ¨parsed



⍝ removing single elements works as follows
⍝ using the example report 8 6 4 4 1
⍝ 
⍝    1 0 1 1 1 / 8 6 4 4 1
⍝ 8 4 4 1
⍝
⍝ placing the 0 in each spot will create all ≢-1 sequences
⍝ the most obvious way to create this is with the identity matrix
⍝ 1 0 0 0 0
⍝ 0 1 0 0 0
⍝ 0 0 1 0 0
⍝ 0 0 0 1 0
⍝ 0 0 0 0 1
⍝ negated so 0s are on the diagonal
⍝ then use each row of the matrix as a mask
