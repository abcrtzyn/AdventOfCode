⎕FIX 'file://../apl_utils/utils.apln'

A ← '#'=↑ Utils.readLines 'Day18/input.txt'

iter←(({+/+/⍵}⌺3 3){(3=⍺)∨(⍵)∧(4=⍺)}⊢) ⍝ iterate once, my attempt at it
iter←({≢⍸⍵}⌺3 3∊¨3+0,¨⊢) ⍝ from apl cart

⍝ part 1
⎕←'Part 1: ', +/+/(iter⍣100) A

corners←(1@(1 1) (100 1) (1 100) (100 100))100 100 ⍴ 0

⍝ part 2
⎕←'Part 2: ', +/+/(corners∘∨∘iter⍣100) A
                  ⍝ after each iteration, put the corners back
