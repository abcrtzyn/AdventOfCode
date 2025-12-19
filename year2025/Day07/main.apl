file ← '.'≠¨ ⊃⎕NGET 'Day07/input.txt' 1

⍝ assuming the S is in the top row and there is nothing else, pretty good assumptions

⍝ ⍵ is the current lasers, ⍺ is the next row
⍝ reduces down to the last row, each step is the current row of lasers.
part1 ← {
    ⍝ rules for this
    ⍝ current  000 010 010 01010
    ⍝ spliters 0x0 000 010 01010
    ⍝ result   000 010 101 10101
    ands ← ⍺ ∧ ⍵ ⍝ splits
    ((~⍺) ∧ ⍵) ∨ (0, ¯1↓ands) ∨ (0,⍨ 1↓ands)
                                ⍝ split path left
                 ⍝ split path right
    ⍝ passthrough
}

⍝ part 1 is counting the number of splits that occur, which is hard in this language
⍝ the way I decided to do it is to use the scan operator to get each the state after each iteration
⍝ and compare it to where the splitters are in the file
⍝ The problem is that the reduction happens right to left and the scan adds items left to right
⍝ The method I came up with is to grab all sets of rows (1), (1 2), (1 2 3)...
⍝ reverse each of them (1), (2 1), (3 2 1)...
⍝ then reduce all of them
⍝ this is no where near as efficent as a normal scan would be

⍝ the result after each iteration
scan ← ⊃¨ part1/¨ ⌽¨,\⊂¨file
                      ⍝ box each row up
                    ⍝ grab sub-lists
                  ⍝ reverse each
          ⍝ reduce each
       ⍝ unbox the results

⍝ a split happens when a laser is present in the row above a splitter
⍝ dropping first and last elements does the row offset needed
⎕←'Part 1: ', +/+/(↑¯1↓scan) ∧ ↑1↓file
                               ⍝ drop the first in file (1s are splitters)
                  ⍝ drop the last in results
                             ⍝ and to find active splits
              ⍝ count it up


⍝ the only difference between this and part1 was replacing or (∨) with plus
⍝ haven't tried it, but part1 might even work with this too.
part2 ← {
    ⍝ rules for this
    ⍝ current  000 0A0 0A0 0A0B0 0AB0
    ⍝ spliters 0x0 000 010 01010 0100
    ⍝ result   000 0A0 A0A A0C0B A0C0
    ⍝ C=A+B
    ands ← ⍺ ∧ ⍵ ⍝ splits
    ((~⍺) ∧ ⍵) + (0, ¯1↓ands) + (0,⍨ 1↓ands)
                                ⍝ split path left
                 ⍝ split path right
    ⍝ passthrough
}

⎕PP ← 15
⍝ much simpler than part 1, just one reduction needed
⎕←'Part 2: ', +/⊃part2/ ⌽file
                        ⍝ reverse
                 ⍝ simulate
              ⍝ count results
