R←⊃⎕NGET 'Day02\input.txt' 1
+/(⌊/+(2∘×+/))2×/↑(⊂1 2 3 1)∘⌷¨↓⍎¨↑('x'∘≠⊆¨⊢)R ⍝ part 1
                                   ⍝ partition with x as delimiter
                                ⍝ convert each cell into a number
                  ⍝ prepare for the next step by getting each combination of l, w, and h
              ⍝ multiply each lw, wh, and hl
      ⍝ sum all sides and multiply by 2 is surface area
   ⍝ take the minimum of the three sides
  ⍝ sum the minimum side with the total surface area
⍝ sum all results for the final answer

⍝ potential for a double map without mix on the hydrant, along with simplifications of for the materialize map

+/(×/+{2×⌊/2+/↑(⊂1 2 3 1)∘⌷¨↓⍵})⍎¨↑('x'∘≠⊆¨⊢)R ⍝ part 2
           ⍝ calculate all possible halfs of perimeters
         ⍝ picks the minimum half perimeter
       ⍝ get the actual perimeter
   ⍝ get the volume
     ⍝ sum the minimum perimeter and volume
⍝ sum all results for the final answer
