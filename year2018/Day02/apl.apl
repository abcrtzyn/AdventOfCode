R←⊃⎕NGET 'Day02/input.txt' 1
×/+/[1]↑(2 3∊{≢⍵}⌸)¨R
⍝ part 2 requires finding two strings with hamming distance 1
{((2⊃⍵)=(1⊃⍵))∘/(1⊃⍵)}((1↑(⍸1=(+/¨∘.≠⍨)))⌷⊢)R
