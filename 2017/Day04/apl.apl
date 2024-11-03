]cd '/Users/aidanchristensen/Documents/AdventOfCode/2017/'
R←⊃⎕NGET 'Day02/input.txt' 1

⍝ part 1
+/((⊢≡∪)' '∘(≠⊆⊢))¨R
                   ⍝ for each line
         ⍝ partition by spaces
   ⍝ is the unique list the same
⍝ sum the results

⍝ part 2
+/((⊢≡∪)(⊂∘⍋⌷⊢)¨∘(' '∘(≠⊆⊢)))¨R
                   ⍝ partition by spaces
         ⍝ sort each word alphabetically
    ⍝ is the unique list the same
⍝ sum the results
