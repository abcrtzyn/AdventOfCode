R←↑⊃⎕NGET 'Day03/input.txt' 1

isnum←(⎕D∊⍨⊢)


⍝ this is applied to the has symbol grid and the character grid to seperate each number
partitionnums← {⊃⍤(,/)(↓isnum ⍺)⊆¨↓⍵}
                        ⍝ partition by the is number grid
                  ⍝ put them all in one array

⍝ part 1
part1 ← {
      ⍝ these are the symbols that are used
      symbols←(⎕D,'.')~⍨∪,⍵
                        ⍝ get all the unique characters
              ⍝ remove the ones that are digits or '.'
      
      ⍝ for each character, determine if there is a symbol near it
      hassymbol←({∨/symbols∊⍵}⌺3 3)⍵

      +/⍎¨ hassymbol {(∨/¨⍺)/⍵}⍥(⍵∘partitionnums) ⍵
                                ⍝ partition the numbers (and the hassymbol)
                       ⍝ select numbers that have at least one symbol
       ⍝ evaluate the numbers and sum them
}
⎕←'Part 1: ', part1 R

part2 ← {
      ⍝ mask surronds the center square
      ⍝ the size 3 7 is the window size to get numbers that are 3 digits
      ⍝ the mask and window size need to change for larger numbers
      mask ← 3 7 ⍴ 0 0 1 1 1 0 0 0 0 1 0 1 0 0 0 0 1 1 1 0 0
      ⍝ a vector of gear structures, filter windows with * in the middle
      gears←(,'*'=⍵)/,({⊂⍵}⌺3 7)⍵
      ⍝ for a gear, get the numbers around that gear, similar to part 1
      gearnums←{⍎¨mask{(∨/¨⍺)/⍵}⍥(⍵∘partitionnums)⍵}
      ⍝ filter * that have only two numbers
      gearfilt←{((⊃2=⍴)¨⍵)/⍵}
      ⍝ finally multiply each gear numbers and add them all up
      +/×/¨gearfilt gearnums¨ gears
}

⎕←'Part 2: ', part2 R
