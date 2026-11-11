
re ← '(\w): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'

input ← ⍉ ↑ ⍎¨ '-' ⎕R '¯' (re ⎕S '\2 \3 \4 \5 \6') ⊃⎕NGET 'Day15/input.txt' 1
                          ⍝ search for re and extract the numbers
                ⍝ replace - with ¯
            ⍝ eval each line (get the numbers)
          ⍝ make a table
        ⍝ transpose

⍝ creates a table of 4 values such that all rows sum to ⍵ and no values are negative
⍝ I would like to have a more efficent way to do this
table ← {↑{(0≤⊣/⍵)/↓⍵}((⍵-+/),⊢)↑,(¯1+⍳1+⍵)(∘.,⍣2)¯1+⍳1+⍵}
                                   ⍝ 0-⍵          ⍝ 0-⍵
                                           ⍝ concat outer product
                                ⍝ table
                      ⍝ add the final column to fulfill the sum property
           ⍝ filter those with negative values

⍝ result for 2
⍝ 2 0 0 0
⍝ 1 0 0 1
⍝ 0 0 0 2
⍝ 1 0 1 0
⍝ 0 0 1 1
⍝ 0 0 2 0
⍝ 1 1 0 0
⍝ 0 1 0 1
⍝ 0 1 1 0
⍝ 0 2 0 0

⎕←'Part 1: ', ⌈/×⌿4↑ 0⌈input+.×⍉ table 100
                      ⍝ inner product with the input
                    ⍝ zero negatives
                 ⍝ take just the properties (not the calories)
                ⍝ multiply to create score
              ⍝ choose the largest



⎕←'Part 2: ', ⌈/×⌿4↑↑[0.5]{(500∘=5⌷[1]⍵)/↓[1]⍵} 0⌈input+.×⍉ table 100
                                                ⍝ inner product and zero negatives (same as part 1)
                            ⍝ select only those where calories is exactly 500 (this doesn't look optimal)
                    ⍝ recreate the table
                 ⍝ take just the properties (not the calories)
                ⍝ multiply to create score
              ⍝ choose the largest
