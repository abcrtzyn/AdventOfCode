enhance←{({pattern[1+2∘⊥∘,⍵]}⌺3 3)⍵}
notenhance←{({pattern[1+2⊥~,⍵]}⌺3 3)⍵}
pad←{⍵@(1+⍳⍴⍵)⊢0⍴⍨2+⍴⍵}
⍝ two times
image3 ← notenhance pad ~(enhance pad image)
twoenhance←{notenhnace pad ~(enhance pad ⍵)}
⍝ 50 times
+/,(twoenhance⍣25) image