⎕FIX 'file://../apl_utils/utils.apln'


input ← Utils.partitionBySpace¨ Utils.readLines 'Day04/input.txt'


⎕← 'Part 1: ', +/(⊢≡∪)¨ input
                        ⍝ for each line
                  ⍝ are all words unique
               ⍝ sum the results


⎕← 'Part 2: ', +/((⊢≡∪)(⊂∘⍋⌷⊢)¨)¨ input
                                ⍝ partition by spaces
                       ⍝ sort each word alphabetically
                   ⍝ are all words unique
               ⍝ sum the results
