
R←↑⊃⎕NGET 'Day01/input.txt' 1
⍝ parsing, .→0 |→1 #→2
Q←(('.'≠⊢)+('#'=⊢))R
