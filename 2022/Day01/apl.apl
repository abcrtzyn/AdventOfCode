]cd 'Documents/AdventOfCode/2022/Day01'
R←⊃⎕NGET 'input.txt' 1


Q←+/¨⍎¨¨({⊃¨0≠⍴¨⍵}⊆⊢)R

⍝ part 1
⌈/Q

⍝ part 2
+/Q[3↑⍒Q]