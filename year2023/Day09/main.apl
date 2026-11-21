
R←⊃⎕NGET 'Day09/input.txt' 1

parsed ← (⍎'¯'@('-'∘=))¨R

⍝ it turns out the next number is equal to coef × the numbers. Stuff to do with binomial expansions.


⍝ generate binomial coefficients for the given length
⍝ not sure if I made this or found it, but it is different from APLCart options
coef←{⍵!⍨¯1+⍳⍵}

linesol←(-/⌽∘(coef∘⍴×⊢))
             ⍝(    ) generate coefficients
                    ⍝ multiply coefficients and input numbers
          
         ⍝alternate positive and negative signs sum
         
⍝ part 1
⎕←'Part 1:' , +/linesol¨ parsed

⍝ part 2, extrapolate backwards. Same as reverse each line
⎕←'Part 2:' , +/linesol¨ ⌽¨ parsed
