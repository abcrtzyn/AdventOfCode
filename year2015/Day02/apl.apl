R←⍎¨↑('x'∘≠⊆¨⊢) ⊃⎕NGET 'Day02/input.txt' 1
      ⍝ partition by x
    ⍝ matrix
  ⍝ eval numbers

⎕←'Part 1: ', +/(⌊/+(2∘×+/))2×/R[;1 2 3 1]
                               ⍝ prepare for the next step by getting each combination of l, w, and h
                            ⍝ multiply each lw, wh, and hl
                    ⍝ sum all sides and multiply by 2 is surface area
                ⍝ take the minimum of the three sides
                  ⍝ sum surface area and minimum side
             ⍝ sum all results for the final answer


min_perimiters ← 2×⌊/2+/R[;1 2 3 1]
                     ⍝ create half permiters
                   ⍝ choose the smallest
                 ⍝ double it
                             
volumes ← ×/ R


⎕←'Part 2: ' , volumes +⍥(+/) min_perimiters
