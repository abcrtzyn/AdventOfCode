
parsed←⍎¨¨(','∘≠⊆⊢)¨⊃⎕NGET 'Day09/input.txt' 1
          ⍝ partion by comma
       ⍝ parse numbers

⎕←'Part 1: ', ⌈/,∘.{×/1+|⍺-⍵}⍨ parsed
                 ⍝ outer product self
                         ⍝ differnce by coordinate
                        ⍝ absolute value
                      ⍝ add 1 to each (inclusive ranges)
                    ⍝ get the area
              ⍝ find the max


