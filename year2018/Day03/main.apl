⎕IO←0
\R←⊃⎕NGET'Day03/input_test.txt' 1
x←⍎¨('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'⎕S'\1 \2 \3 \4 \5')R
+/+/2≤⊃+/{(1∘+@((1↓3↑⍵)∘+¨⍳(¯2↑⍵)))1100 1100⍴0}¨x

⍝ part 2 is about looking for overlap
⍝ rather than compare each grid to each other grid,
⍝ compare endpoints

⍝
⍝   1 3 4 4 → [1 5] [3 7]
⍝   3 1 4 4 → [3 7] [1 5]
⍝   5 5 2 2 → [5 7] [5 7]
⍝
⍝   single direction non-overlap if 
⍝   a_end ≤ b_start or a_start ≥ b_end
⍝   single direction overlap if
⍝   a_end > b_start and a_start < b_end
⍝   overlap if true in both directions
⍝   non-overlap if non-overlap in one direction
⍝   ax_start ≥ bx_start+bx_len or 
⍝   bx_start ≥ ax_start+ax_len or 
⍝   ay_start ≥ by_start+by_len or 
⍝   by_start ≥ ay_start+ay_len 

nonoverlap←{∨/(⍺[1],⍺[2],⍵[1],⍵[2]) ≥ (⍵[3],⍵[4],⍺[3],⍺[4])+(⍵[1],⍵[2],⍺[1],⍺[2])}
1+⍸(⌈/=⊢)+/∘.nonoverlap⍨x ⍝ using the fact that the input is ordered and complete
⍝ if the input is not ordered and complete, use the where to index into x to get the initial claim ID
