key ← ⍎⊃⊃⎕NGET 'Day10/input.txt' 1


input ← (10∘⊥⍣¯1) key

⍝ takes in an array of digits and outputs what it sees
⍝ runs of more than 10 never
looksay←{∊(≢,⊃)¨({+\2≠/0,⍵}⊆⊢)⍵}
                    ⍝ find all points that aren't equal
                           ⍝ partition the input
           ⍝ create tuples of counts, digit
        ⍝ concatenate it all together

res1 ← (looksay⍣40) input

⎕←'Part 1: ' , ≢res1
⍝ takes a bit of time
⎕←'Part 2: ' , ≢(looksay⍣10) res1
