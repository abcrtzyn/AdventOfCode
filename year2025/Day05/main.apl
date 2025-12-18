file ← ⊃⎕NGET 'Day05/input.txt' 1
split ← (''∘≢¨⊆⊢)file
        ⍝ split the file into the two sections by seeing where the double newline is
ranges ← 0 1∘+¨ ⍎¨¨('-'∘≠⊆⊢)¨1⊃split
                             ⍝ get the first section
                    ⍝ partition each line by -
                ⍝ convert all numbers
         ⍝ add 1 to the end of the ranges for interval index
ids ← ⍎¨2⊃split
      ⍝ convert each line to a number

⎕←'Part 1: ', +/∨⌿1= ↑⍸∘ids ¨ranges
                      ⍝ interval index on all ids for all ranges
                     ⍝ make it a table
                  ⍝ if within the range
                ⍝ or reduce each ID
              ⍝ count it


⍝ part 2 is actually quite difficult to do in an array based language becuase it needs a loop that needs state between iterations.
⍝ I'll give it an attempt here.

⍝ ⍵ current least value unchecked and count, ⍺ next range to process
⍝ we are doing a non-commutative reduce function where ⍵ keeps the state
⍝ this is actually a useful construct that I wish was easier in this language
part2 ← {
    count ← ⍵[1]
    curr ← ⍵[2]
    low ← ⍺[1]
    high ← ⍺[2]

    ⍝ if curr is less than low, count the whole range
    curr < low: (count+high-low) (high)
    ⍝ if curr is greater than low but less than high, count curr to high
    curr < high: (count+high-curr) (high) 
    ⍝ if curr is greater than high, everything in the range is counted, do nothing
    count curr
}

⎕PP ← 16
⎕←'Part 2: ', 1⊃⊃ part2/ (⊂0 0) ,⍨ (⊂∘⍒⌷⊢) ranges
                                   ⍝ sort in reverse order, from APLcart
                         ⍝ tack 0 0 on the back to start prime the accumlator and state
                  ⍝ reduce
              ⍝ take the sum only
