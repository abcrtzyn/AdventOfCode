]cd '/Users/aidanchristensen/Documents/AdventOfCode/2017/'
R←⍎¨⊃⎕NGET 'Day02/input.txt' 1

⍝ part 1
+/(⌈/-⌊/)¨R

⍝ part 2
⍝ create an identity matrix the same size as the left argument
ident←(⌽⍤⍴⍴1↑⍨1+≢)


+/(÷/((⍸∘⍉((ident≠⊢)0=∘.|⍨))⌷⊢))¨R
                                ⍝ for each row
                       ⍝ take the mod of every pair
                    ⍝ find the divisible pair
           ⍝ not the diagonal 5/5=1
        ⍝ transpose to get big/little
       ⍝ get indicies
                           ⍝ get those indicies
  ⍝ divide reduce the two numbers
⍝ sum all rows
