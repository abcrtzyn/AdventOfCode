weapons ← 2⊃¨ ('dagger' (8 4 0)) ('shortsword' (10 5 0)) ('warhammer' (25 6 0)) ('longsword' (40 7 0)) ('greataxe' (74 8 0))
armour ← 2⊃¨ ('none' (0 0 0)) ('leather' (13 0 1)) ('chainmail' (31 0 2)) ('splintmail' (53 0 3)) ('bandedmail' (75 0 4)) ('platemail' (102 0 5))
rings ← 2⊃¨ ('none' (0 0 0)) ('damage1' (25 1 0)) ('damage2' (50 2 0)) ('damage3' (100 3 0)) ('defense1' (20 0 1)) ('defense2' (40 0 2)) ('defense3' (80 0 3))

options ← , weapons ∘.+ armour ∘.+ (,(1@(1 1))~(,⍨⍴1↑⍨1∘+) ≢ rings) / , ∘.+ ⍨rings
                                                                        ⍝ two rings
                                                                      ⍝ ravel
                                   ⍝ select all two rings options that aren't duplicates
                                   ⍝ two nones is alowed
            ⍝ cross with weapons and armour too
          ⍝ ravel

ph ← 100

R ← ⊃ ⎕NGET 'Day21/input.txt' 1
(bh bd ba) ← ⍎¨2⌷[2]↑':'(~⍤∊⍨⊆⊢)¨R

player_won←({⌈bh÷1⌈(2⊃⍵)-ba}≤{⌈ph ÷ 1⌈bd-(3⊃⍵)})¨options
                              ⍝ the number of turns to kill the player
             ⍝ the number of turns to kill the boss
                            ⍝ player turns are less

⍝ this is the cost of each option
costs←1⊃¨options

⍝ select the minimum cost on player_won games
⎕←'Part 1: ', ⌊/player_won/costs
⍝ select the max cost on boss won games
⎕←'Part 2: ', ⌈/(~player_won)/costs
