
R←⊃⎕NGET 'Day04/input.txt' 1

⍝ part 1
⎕← 'Part 1: ', +/((⊢≡∪)' '∘(≠⊆⊢))¨R
                                 ⍝ for each line
                       ⍝ partition by spaces
                   ⍝ are all words unique
               ⍝ sum the results

⍝ part 2
⎕← 'Part 2: ', +/((⊢≡∪)(⊂∘⍋⌷⊢)¨∘(' '∘(≠⊆⊢)))¨R
                                ⍝ partition by spaces
                      ⍝ sort each word alphabetically
                 ⍝ are all words unique
             ⍝ sum the results
