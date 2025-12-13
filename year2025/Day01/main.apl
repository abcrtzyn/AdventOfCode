file←⊃⎕NGET'Day01/input.txt' 1

rotations ← ((2×¯0.5+'R'=⊃¨) × (⍎¨1↓¨⊢)) file
                                    ⍝ for each line
                                  ⍝ drop the L or R
                                ⍝ read as number
                         ⍝ get only the L or R
                     ⍝ boolean is R
              ⍝ shift L is ¯1 and R is 1
                            ⍝ multiply

positions ← +\ 50 , rotations

⍝ find all the spots where positions mod 100 is zero and count them
⎕ ← 'Part 1: ', +/0=100|positions

⍝ finding border crossings on 100 boundary.
⍝ dividing by 100 nearly gives the number of turns have been done to the lock.
⎕ ← 'Part 2: ', 2÷⍨ (+/| 2-/ ⌊100÷⍨ positions)+(+/| 2-/ ⌊100÷⍨ ¯1+positions)
                             ⍝ divide by 100                    ⍝ offset by 1
                             ⍝ and floor
                        ⍝ windowed subtract
                     ⍝ count all

⍝          +/|2-/ ⌊100 ÷⍨ positions    +/|2-/ ⌊100 ÷⍨ ¯1+positions
⍝ 99 0  1           counted                     counted
⍝ 99 0 99        double counted               not counted
⍝  1 0  1          not counted               double counted

