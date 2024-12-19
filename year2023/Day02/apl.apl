
R←⊃⎕NGET 'Day02/input.txt' 1

⍝ after completing both parts, it is clear that ; and , sepeators are not important
⍝ we only need the indicies and number color pairs

⍝ parse each line into | index | pairs
lineparser←{
     id str←(':'∘≠⊆⊢)5↓⍵
     pairs←((⍎1∘⊃),(⊂2∘⊃))¨' '(≠⊆⊢)¨',;'(~⍤∊⍨⊆⊢)str
     (⍎id) pairs
}

parsed ← ↑lineparser¨R

⍝part 1


⍝ check returns if the entry is below the number of cubes
⍝ given a vector of structures like  | 'nn' | 'red' |
check←{
     data←↑⍵
     nums←data[;1]
     ⍝ converts a vector of colors into their maximums
     maxs←12 13 14['red' 'green' 'blue'⍳data[;2]]
     
     ∧/nums≤maxs
}

⍝ there are multiple ways to think about this in arrays
⎕ ← 'Part 1:',+/{(check¨⍵[;2])/⍵[;1]}parsed
                                ⍝ line indicies
                       ⍝ for each line
              ⍝ sum all lines




⍝ part 2
⍝ this is about getting the maximum for each color for each game
⍝ I totally forgot about grouping
⍝ this solution is much simpiler than what is below

⎕ ← 'Part 2: ' , +/ {×/ (↑⍵)[;2] {⌈/⍵}⌸ (↑⍵)[;1]}¨ parsed[;2]
                                                  ⍝ only look at the pairs
                                                 ⍝ for each line
                                        ⍝ the number
                         ⍝ the color
                                     ⍝ group numbers by color
                                 ⍝ take the max in each group
                    ⍝ multiply for each line
                 ⍝ sum lines




⍝ maxcolor←{
⍝      ⍝ given a color ⍺ and pairs ⍵
⍝      ⍝ return the maximum number of that color
⍝      table ← ↑⍵
⍝      counts ← 1⌷[2]table
⍝      colors ← 2⌷[2]table
⍝      ⌈/ ((⊂⍺)≡¨colors)/counts
⍝      ⍝ maxiumum of all counts associated with a color
⍝ }

 
⍝ ⎕←'Part 2:', +/×⌿'red' 'green' 'blue'∘.maxcolor 2⌷[2] parsed
                                                ⍝ only need the pairs for each line
                        ⍝ for each line, get the max for each color
               ⍝ multiply the colors
             ⍝ sum the lines
