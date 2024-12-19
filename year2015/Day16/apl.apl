⍝ INCOMPLETE SOLUTION

keys ← 'children' 'cats' 'samoyeds' 'pomeranians' 'akitas' 'vizslas' 'goldfish' 'trees' 'cars' 'perfumes'
values ← 3 7 2 3 0 0 5 3 2 1


R ← ⊃ ⎕NGET 'Day16/input.txt' 1

⍝ there are always three properties for each sue, so 1 1 2 2 3 3 is just fine for this
intermediate_parse ← ' ,:'∘(~⍤∊⍨⊆⊢)¨R

⍝ in this case, sues is just ⍳500, but it is here for completeness
sues ← ⍎¨ 2⊃¨ intermediate_parse

parsed← ↑¨ 1 1 2 2 3 3∘⊆¨2↓¨ intermediate_parse

⍝ There is a nice inner product solution using this table
⍝ but I can't figure out how to make it
⍝  1 ¯1 ¯1 ¯1 ¯1  7 ¯1 ¯1  8 ¯1
⍝  5 ¯1 ¯1 ¯1 10 ¯1 ¯1 ¯1 ¯1 10
⍝ ¯1 ¯1 ¯1  4 ¯1  1 ¯1 ¯1  5 ¯1
⍝ ...

⍝ If I was, the following would solve it
⍝ x ← 4 10 ⍴ 1 ¯1 ¯1 ¯1 ¯1 7 ¯1 ¯1 8 ¯1 5 ¯1 ¯1 ¯1 10 ¯1 ¯1 ¯1 ¯1 10 ¯1 ¯1 ¯1 4 ¯1 1 ¯1 ¯1 5 ¯1 3 ¯1 ¯1 ¯1 ¯1 0 5 ¯1 ¯1 ¯1
⍝ ⍸ values ∧.{(⍺=⍵)∨¯1=⍵} ⍉x

part1match←{
    v←⍎¨⍵[;2]
    x←values[keys⍳⍵[;1]]
    v≡x
}

⎕←'Part 1: ', ⊃ sues[⍸ part1match ¨parsed]
            ⍝ ⊃ assumes there is only one match

⍝ part 2 requires doing different comparisons on each trait
⍝ which is not easy in APL
