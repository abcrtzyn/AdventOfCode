parsed←⍎¨⊃⎕NGET'Day03/input.txt' 1
⍝ 3 numbers per line

⍝ from aplcart. works the same as ⍴ but a missing dimension is allowed
⍝ and it will figrue out the size for that dimension. I definitely will be using this more
rho_smart ← {⍵⍴⍨⍺×@(<∘0)⍨(×/⍴⍵)÷×/⍺~0}


⍝ returns boolean for if the set of 3 numbers is valid
triangle_valid ← ((2×⌈/)<+/)


⍝ z < x+y where z is the longest side
⍝ so 2z < x+y+z
⎕← 'Part 1: ', +/triangle_valid¨parsed
               ⍝ count valid triangles

⍝ part 2 requires transposing sections
⎕← 'Part 2: ', +/ triangle_valid¨ ↓ ¯1 3 rho_smart ⍉ ↑ parsed
                                                     ⍝ ungroup
                                                   ⍝ transpose to get triangles lengths next to each other
                                    ⍝ reshape into rows of 3, dont care how many
                                  ⍝ regroup
                ⍝ count valid triangles
