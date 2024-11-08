
R ← ⊃ ⎕NGET 'Day09/input.txt' 1

↑((~(' to '∘stringFind∨' = '∘stringFind))⊆⊢)¨R
⍝ create a distance matrix
⍝ 0    LtoD LtoB
⍝ DtoL 0    DtoB
⍝ BtoL BtoD 0

⍝ index into the matrix
⍝ sum elements

⍝ there are some great APL Cart and dfns workspace stuff that I will try and use later
