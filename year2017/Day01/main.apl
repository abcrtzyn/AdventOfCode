
R←⊃⊃⎕NGET 'Day01/input.txt' 1

⎕ ← 'Part 1: ' , {+/⍎¨(⍵=1⌽⍵)/⍵}R
                         ⍝ rotate 1
                       ⍝ equal to
                            ⍝ compress
                    ⍝ evaluate digits
                  ⍝ sum

⍝ a tacit free version
⍝ +/⍎¨((⊢=1∘⌽)⊢⍤/⊢)


⎕ ← 'Part 2: ' , {+/⍎¨(⍵=(2÷⍨⍴⍵)⌽⍵)/⍵}R
⍝ exact same expect        rotate by half the length


⍝ and a tacit free version of it, 4 nested 3 trains
⍝  +/⍎((⊢=((2÷⍨⍴)⌽⊢))⊢⍤/⊢)
⍝
⍝       ((⊢=((2÷⍨⍴)⌽⊢))⊢⍤/⊢)
⍝   ┌─3─train──┼─┐
⍝ ┌3┼train┐    ⍤ ⊢
⍝ ⊢ = ┌3tr┼─┐ ┌┴┐
⍝   ┌3┼t┐ ⌽ ⊢ ⊢ /
⍝   2 ⍨ ⍴
⍝   ┌─┘
⍝   ÷
