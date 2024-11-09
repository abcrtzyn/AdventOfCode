⍝ TODO: PARSE INPUT

w←5 4 ⍴3 ¯3 ¯1 0 0 3 0 0 0 0 4 ¯2 ¯3 0 0 2 2 9 1 8 ⍝ as input
⎕←⌈/×⌿4↑0⌈w+.×⍉↑{(0≤⊣/⍵)/↓⍵}((100-+/),⊢)↑,(∘.,⍣2)⍨¯1+⍳100 ⍝ part 1
                                          ⍝ create a grid of vectors
                                        ⍝ concatenate and mix them all
                             ⍝ prepend 100-sum to make all add to 100
                 ⍝ remove the ones with a negative ingredent
          ⍝ inner product with the properties matrix
        ⍝ zero anything negative
    ⍝ multiply to get score
  ⍝ take maximum score

⎕←⌈/×⌿4↑↑[0.5]{(500∘=5⌷[1]⍵)/↓[1]⍵}0⌈w+.×⍉↑{(0≤⊣/⍵)/↓⍵}((100-+/),⊢)↑,(∘.,⍣2)⍨¯1+⍳100 ⍝ part 2
