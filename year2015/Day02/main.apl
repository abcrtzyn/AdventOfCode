⎕FIX 'file://../apl_utils/utils.apln'

⍝ parse the numbers in each line seperated by an x, return as a table
input ← ↑ 'x'∘Utils.parseNumbers¨ Utils.readLines 'Day02/input.txt'




⎕←'Part 1: ', +/(⌊/+(2∘×+/))2×/input[;1 2 3 1]
                               ⍝ prepare for the next step by getting each combination of l, w, and h
                            ⍝ multiply each lw, wh, and hl
                    ⍝ sum all sides and multiply by 2 is surface area
                ⍝ take the minimum of the three sides
                  ⍝ sum surface area and minimum side
             ⍝ sum all results for the final answer


min_perimiters ← 2×⌊/2+/input[;1 2 3 1]
                     ⍝ create half permiters
                   ⍝ choose the smallest
                 ⍝ double it
                             
volumes ← ×/ input


⎕←'Part 2: ' , volumes +⍥(+/) min_perimiters
