
R←⊃⎕NGET 'input.txt' 1

+/{+/+/¨(('#'≠⍵)⊆⍳⍴⍵)/⍨¨{⍵[⍋⍵]}¨('#'≠⍵)⊆'O'=⍵}¨↓⌽⍉↑R