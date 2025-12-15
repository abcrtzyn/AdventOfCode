parsed ← ⍎¨¨ ⊃⎕NGET 'Day03/input.txt' 1
         ⍝ turn each digit into a number (wish max worked on characters)

⍝ given a list of numbers, finds the largest 2 digit number
part1 ← {
    first_digit ← ⌈/ ¯1↓⍵
                     ⍝ drop the last digit
                  ⍝ choose the max digit

    second_digit ← ⌈/ ⍵ ↓⍨ ⍵ ⍳ first_digit
                            ⍝ get the (first) index of the max digit
                        ⍝ cut off everything before it
                   ⍝ choose the max digit of what is left
    
    ⍝ create the number
    second_digit + 10 × first_digit
}

⎕← 'Part 1: ', +/ part1¨ parsed
               ⍝ sum the results

⍝ this is similar, but now there needs to be some recursive method to do it
⍝ this is tail recursive function, so good optimization internally
part2_internal ← {
    ⍝ ⍺ is the result number
    ⍝ ⍵ is number of digits and the string to grab from
    
    cut ← ⍵[1]-1                ⍝ how many digits need to be cut off the end of the string, 1 less than the digits we need
    list ← ⊃⍵[2]                ⍝ the string of digits
    dig ← ⌈/ (-cut) ↓ list      ⍝ drop the cut and pick the largest
    new ← list ↓⍨ list ⍳ dig    ⍝ create the next list by removing all digits before the max digit
    cut≤0: dig+10×⍺             ⍝ if we are at the end, return the answer
    (dig+10×⍺) ∇ cut (new)      ⍝ else recurse with the new list and answer so far
}

⍝ header function to deal with the tuple ⍵ argument
part2 ← {
    ⍝ ⍺ is the iterations
    ⍝ ⍵ is the list
    0 part2_internal ⍺ ⍵
}

⎕PP ← 15
⎕ ← 'Part 2: ', +/ 12 part2¨ parsed
                ⍝ sum the results        

⍝ optional part 1 using part2 solution
⍝ ⎕← 'Part 1: ', +/ 2 part2¨ parsed

