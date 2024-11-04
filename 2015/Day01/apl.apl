R←⊃⊃⎕NGET 'Day1\input.txt' 1
('('∘=-⍥(+/)')'∘=)R ⍝ part1  3 train minus
⊃⍸¯1=+\1-⍨2×'('∘= R ⍝ part2
