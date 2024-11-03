⎕io ← 0

]cd '/Users/aidanchristensen/Documents/AdventOfCode/2023/Day13'
R←⊃⎕NGET 'input.txt' 1

grids←↑¨(''∘≢¨⊆⊢)R

slices←{↑0=⍸∘(⍳⍵)¨↓((-⍵-2)+2×⍳(⍵-1)),[0.5](1+⍳(⍵-1))}

⍝ columns
+/⊃¨1+⍸¨((slices 1∘⊃∘⍴){((⊣⌷⊢)(⊣≡⌽⍤⊢)⍥(/∘⍵)(⊣⌷⌽∘⊖⍤⊢))∘⍺¨⍳⊃⍴⍺}⊢)¨grids

⍝ transpose for rows
+/⊃¨1+⍸¨((slices 1∘⊃∘⍴){((⊣⌷⊢)(⊣≡⌽⍤⊢)⍥(/∘⍵)(⊣⌷⌽∘⊖⍤⊢))∘⍺¨⍳⊃⍴⍺}⊢)¨⍉¨grids
⍝ manually compte the sum

⍝ part 2
⍝ columns
+/⊃¨1+⍸¨((slices 1∘⊃∘⍴){1∘=¨+/¨+/¨((⊣⌷⊢)(⊣≠⌽⍤⊢)⍥(/∘⍵)(⊣⌷⌽∘⊖⍤⊢))∘⍺¨⍳⊃⍴⍺}⊢)¨grids

⍝ transpose for rows
+/⊃¨1+⍸¨((slices 1∘⊃∘⍴){1∘=¨+/¨+/¨((⊣⌷⊢)(⊣≠⌽⍤⊢)⍥(/∘⍵)(⊣⌷⌽∘⊖⍤⊢))∘⍺¨⍳⊃⍴⍺}⊢)¨⍉¨grids