⎕FIX 'file://../apl_utils/utils.apln'

input ← Utils.readSingleLine 'Day12/input.txt'

⍝ part 1
⎕ ← 'Part 1: ', +/ Utils.parseNumbersVector ({∨⌿('-',⎕D)∘.=⍵}⊆⊢) input

⍝ I would like to make an efficient way of parsing a JSON to get the values without red
