⎕FIX 'file://../apl_utils/utils.apln'

⍝ read the file and conver 
input ← Utils.toDigits Utils.readSingleLine 'Day01/input.txt'

⎕ ← 'Part 1: ' , ((⊢=1∘⌽)⍛(+.×)) input


⍝ other methods
⍝ {+/(⍵=1⌽⍵)/⍵}
⍝ dot product
⍝ ((⊢=1∘⌽)+.×⊢)

⍝ +/ (⊢(/⍨)⊢=1∘⌽)
⍝ 



⎕ ← 'Part 2: ' , ((⊢=(2÷⍨≢)⌽⊢)⍛(+.×)) input

⍝ other methods
⍝ {+/(⍵=(2÷⍨⍴⍵)⌽⍵)/⍵}
⍝ +/((⊢=((2÷⍨⍴)⌽⊢))⊢⍤/⊢)
