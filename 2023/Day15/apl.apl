
R←⊃⎕NGET 'input.txt' 1

⍝ for strings less than 12 charecters
hash←{256|+/(256|17*⍳⍴⍵)×⌽⎕UCS ⍵}

⍝ part 1
+/hash¨(','∘≠⊆⊢)R
