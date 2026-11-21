text ← ↑⊃ ⎕NGET 'Day04/input.txt' 1

⍝ determines if the diagonals of a 4x4 grid have the string XMAS or backwards
diag ← {
    ⍝ get the diagonals
    forward  ← 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 /, ⍵
    backward ← 0 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0 /, ⍵
    ⍝ sum the occurances if they are XMAS or XMAS backwards
    +/+/ 'XMAS' 'SAMX' ∘.≡ forward backward
}

⍝ determines how many occurances of XMAS there are
xmas ← {
    vertical ← +/+/({+/ 'XMAS' 'SAMX' ≡¨ ⊂,⍵}⌺4 1) text
    horizontal ← +/+/({+/ 'XMAS' 'SAMX' ≡¨ ⊂,⍵}⌺1 4) text
    diagonals ← +/+/(diag⌺4 4) text

    vertical + horizontal + diagonals
}

⎕←'Part 1: ', xmas text

⍝ given a 3x3 grid, determines if it is a MAS X
masxbool ← {
    ∧/(∨/ 'MS' 'SM' ≡¨ ⊂ ⍵[1;1], ⍵[3;3]) (∨/ 'MS' 'SM' ≡¨ ⊂ ⍵[1;3], ⍵[3;1]) (⍵[2;2]='A')
       ⍝ forward diagonal is MS or SM     ⍝ reverse diagonal is MS or SM    ⍝ center is an A
    ⍝ all are true
      
}

⎕←'Part 2: ', +/+/(masxbool⌺3 3)text
