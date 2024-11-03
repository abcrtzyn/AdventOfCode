weapons ← ('dagger' (8 4 0)) ('shortsword' (10 5 0)) ('warhammer' (25 6 0)) ('longsword' (40 7 0)) ('greataxe' (74 8 0))
armour ← ('none' (0 0 0)) ('leather' (13 0 1)) ('chainmail' (31 0 2)) ('splintmail' (53 0 3)) ('bandedmail' (75 0 4)) ('platemail' (102 0 5))
rings ← ('none' (0 0 0)) ('damage1' (25 1 0)) ('damage2' (50 2 0)) ('damage3' (100 3 0)) ('defense1' (20 0 1)) ('defense2' (40 0 2)) ('defense3' (80 0 3))

ph ← 100

bh←103
ba←2
bd←9

⍝ this includes some invalids (two of the same ring)
options←weapons∘.{(⍺,⍥(1∘⊃)⍵)(⍺+⍥(2∘⊃)⍵)}armour∘.{(⍺,⍥(1∘⊃)⍵)(⍺+⍥(2∘⊃)⍵)}rings∘.{(⍺,⍥(1∘⊃)⍵)(⍺+⍥(2∘⊃)⍵)}rings
costs←1∘⊃¨2⊃¨options

mask1←({⌈bh÷(2⊃⍵)-ba}≤{⌈ph÷0.0001+bd-(3⊃⍵)})¨2⊃¨options
⌊/mask1/⍥,costs

mask2←({⌈bh÷(2⊃⍵)-ba}>{⌈ph÷0.0001+bd-(3⊃⍵)})¨2⊃¨options
⌈/mask2/⍥,costs
⍝ also check that the triggerer does not land on the diagonal of duplicate rings


6,4