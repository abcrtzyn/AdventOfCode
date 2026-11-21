


R←⊃⎕NGET 'Day01/input.txt' 1

⍝ part 1

⍝ given a line, return the calibration value
part1line ← {⍎(⊃,(⊃⌽))⍵/⍨⎕D∊⍨⍵}
                         ⍝ where are the digits
                      ⍝ mask the digits
              ⍝ concat first and last digits
             ⍝ turn it into a number

⎕← 'Part 1:', +/ part1line ¨R



⍝ part 2
⍝ how strings map to numbers
strings ← 'one' 'two' 'three' 'four' 'five' 'six' 'seven' 'eight' 'nine' '1' '2' '3' '4' '5' '6' '7' '8' '9'
numbers ← 18 ⍴ '1' '2' '3' '4' '5' '6' '7' '8' '9'

part2line ← {
      ⍝ the first number in each is the index in the line
      ⍝ the second number is the index in strings that was found
      ⍝ it appears that the first numbers will always be in sorted order
      indicies ← ⍸⍉↑strings⍷¨⊂ ⍵
      ⍎numbers[(⊃,(⊃⌽)) 2⊃¨indicies]
               ⍝ use the first and last of the indicies
      ⍝ get the associated numbers catinated and make them a number
}

⎕← 'Part 2:', +/ part2line ¨R
