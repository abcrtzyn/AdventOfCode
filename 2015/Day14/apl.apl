R←⊃⎕NGET 'C:\Users\tater\Documents\AdventOfCode\2015\Day14\input.txt' 1
⌈/↑2503{⍵[2]×+/⍺⍴⍵[3]≥⍳⍵[3]+⍵[4]}¨↓{((⊂1)⌷[2]⍵),(⍎¨(⊂4 7 14)⌷[2]⍵)}↑' '(≠⊆⊢)¨R ⍝ part 1
⌈/+/(⊢=9 2503⍴⌈⌿)↑2503{+\⍵[2]×⍺⍴⍵[3]≥⍳⍵[3]+⍵[4]}¨↓{((⊂1)⌷[2]⍵),(⍎¨(⊂4 7 14)⌷[2]⍵)}↑' '(≠⊆⊢)¨R ⍝ part 2
⍝ possible improvements
       ⍝ calculated number of reindeer
         ⍝ one input for time