
⍝ get the coordinates of all '#'
grid←'#'=↑⊃⎕NGET'Day11/input.txt' 1
indicies←↑⍸grid

⍝ this function should provide the right indicies even for higher dimensions

⍝ takes in an offset(number of cells that in cell stands for) and the boolean grid
modifyindexs←{
    offset←⍺-1
    ⍝ get the indicies by dimension
    indicies←↓⍉↑⍸⍵
    ⍝ reduce the grid by dimension
    reductions← ~{(∨⌿⍤⍺)⍵}∘⍵¨⍳⍴⍴⍵
                              ⍝ for each dimension
                   ⍝ or reduce on that axis
                ⍝ or reduce

    ⍝ for each in indicies and reductions
    ↓⍉↑reductions{⍵+(+\offset×⍺)[⍵]}¨indicies
                       ⍝ multiply offset
                     ⍝ scan cummulative additions
                                ⍝ index by the indicies
                  ⍝ add the indicies
    ⍝ undo shift the indices
} 

⍝ standard taxicab metric given two vectors
⍝ taxicab←(+/⍤|⍤-)
taxicab←(1⊥∘|-)

⎕←'Part 1:' , 2÷⍨+/+/∘.taxicab⍨  2 modifyindexs grid
⎕PP←14
⎕←'Part 2:' , 2÷⍨+/+/∘.taxicab⍨  1000000 modifyindexs grid
