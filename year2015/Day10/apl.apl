                  ⍝ INPUT HERE
input ← (10∘⊥⍣¯1) 211

⍝ takes in an array of digits and outputs what it sees
⍝ runs of more than 10 never
looksay←{∊(≢,⊃)¨({+\2≠/0,⍵}⊆⊢)⍵}
                    ⍝ find all points that aren't equal
                           ⍝ partition the input
           ⍝ create tuples of counts, digit
        ⍝ concatenate it all together

⎕←'Part 1: ' , ≢(looksay⍣40) input
⍝ takes a bit of time
⎕←'Part 2: ' , ≢(looksay⍣50) input
