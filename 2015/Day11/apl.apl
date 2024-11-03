LettersToNumbers ← {¯1+'abcdefghijklmnopqrstuvwxyz'⍳⍵}
NumbersToLetters ← {'abcdefghijklmnopqrstuvwxyz'[1+⍵]}

IncrementPassword←{26 26 26 26 26 26 26 26⊤1+26⊥⍵}

HasIncrement←{∨/2∧/2(⊢(1=-)⊣)/⍵}
HasTwoPair←{∨/∨/(⊢∘.≠⊢){(0,2=/⍵)/⍵}⍵}
NotHasILO←{~∨/8 11 14 ∊ ⍵}
IsValid←{∧/(HasTwoPair ⍺) (NotHasILO ⍺) (HasIncrement ⍺)}

NumbersToLetters (IncrementPassword⍣IsValid) LettersToNumbers 'string' ⍝ part 1
NumbersToLetters ((IncrementPassword⍣IsValid)⍣2) LettersToNumbers 'string' ⍝ part 2