]cd '/Users/aidanchristensen/Documents/AdventOfCode/2023/Day14'
R←⊃⎕NGET 'input.txt' 1

+/{+/+/¨(('#'≠⍵)⊆⍳⍴⍵)/⍨¨{⍵[⍋⍵]}¨('#'≠⍵)⊆'O'=⍵}¨↓⌽⍉↑R