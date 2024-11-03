⍝ The formula for a given cell (x,y)
⍝ = minus 5 from hundreds digit ((x+10)*y+serial)*(x+10)
⍝ simplifying  (xxy+10xy+x*serial)+(10xy+100y+10*serial)
⍝              
⍝       or     (x+10)(x+10)*y+(x+10)serial

rack←10+⍳300
y←⍳300

⍸(⊢=(⌈/⌈/))({+/+/⍵}⌺3 3)⌊100÷⍨1000|(300 300⍴1000|810×rack)+1000|y∘.×2*⍨rack
⍝ the result is swapped coordinates and -1,-1
⍝ so if the program gives 15 246, the answer is 245,14 

⍝ for part 2, I really just trialed all stencil sizes until I found the max
⍝ then I created a grid made of coordinates to get the upper left square coordinate
(⍳300)∘.,(⍳300)
