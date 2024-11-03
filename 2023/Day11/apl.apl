
R←⊃⎕NGET 'Day11/input.txt' 1

grid←'#'=↑R
⍝ part 1
modind1←↓⍉({(1⌷[2]↑⍵)+(+⍀~∨/grid)[1⌷[2]↑⍵]},[0.5]{(2⌷[2]↑⍵)+(+⍀~∨⌿grid)[2⌷[2]↑⍵]})⍸grid
⍝ part 2
modind2←↓⍉({(1⌷[2]↑⍵)+(+⍀999999×~∨/grid)[1⌷[2]↑⍵]},[0.5]{(2⌷[2]↑⍵)+(+⍀999999×~∨⌿grid)[2⌷[2]↑⍵]})⍸grid

⍝ standard taxicab metric given two vectors
⍝ taxicab←(+/⍤|⍤-)
taxicab←(1⊥∘|-)

⎕←'Part 1:' , 2÷⍨+/+/∘.taxicab⍨ modind1
⎕PP←14
⎕←'Part 2:' , 2÷⍨+/+/∘.taxicab⍨ modind2
