]cd 'Documents/AdventOfCode/2022'

R←⊃⎕NGET 'Day03/input.txt' 1

ALPHA←(⎕UCS 97+⍳26),⎕A

⍝ part 1
+/1+ALPHA⍳(((2÷⍨⍴)↑⊢)(⊃∩)(2÷⍨⍴)↓⊢)¨ R

⍝ part 2
+/1+ALPHA⍳⊃¨(↑∩/)¨{((⍴⍵)⍴1 0 0)⊂⍵}R