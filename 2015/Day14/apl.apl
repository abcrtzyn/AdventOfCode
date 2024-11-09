R←⊃⎕NGET 'Day14/input.txt' 1

re ← '\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.'

parsed ← ⍎¨(re ⎕S '\1 \2 \3')R



⎕←'Part 1: ', ⌈/2503{⍵[1]×+/⍺⍴⍵[2]≥⍳⍵[2]+⍵[3]}¨ parsed
                                   ⍝ create a cycle worth of indices
                              ⍝ make boolean mask for when the index is greater than the fly time
                             ⍝ reshape to the requested race length
                          ⍝ sum the number of flying times
                     ⍝ multiply by the fly speed
              ⍝ take the maximum of all of them

⎕←'Part 2: ', ⌈/(⊢+.=⌈⌿) ↑ 2503{⍵[1]×+\⍺⍴⍵[2]≥⍳⍵[2]+⍵[3]}¨ parsed
                                        ⍝ same as part 1
                                     ⍝ scan sum the number of flying times
                               ⍝ multiply by the fly speed
                     ⍝ find the max for each index
                 ⍝ find all the times where it is equal and count them
              ⍝ get the max of the final scores

⍝ I'm super happy with the inner product, not often do I have a use for it, espcially in AoC
