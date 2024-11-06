R←⊃⎕NGET 'Day05/input.txt' 1

⍝ Part 1
⍝ given a string, returns a boolean if the property is true
⍝ has3vowels←(3≤(+/'aeiou'∊⍨⊢))
⍝ hasDoubleLetter←(∨/(2=/⊢))
⍝ this one also takes in a list of substrings as ⍺
⍝ hasStrings←{∨/∨/¨⍷∘⍵¨ ⍺}

⍝ this is a function that goes per string
⍝ ⎕← 'Part 1: ', +/{(hasDoubleLetter ⍵)∧(has3vowels ⍵)∧~('ab' 'cd' 'pq' 'xy')hasStrings ⍵}¨R ⍝ part 1

⍝ this solution has a little bit more array based
vowels ← 3≤+/¨'aeiou'∘(∊⍨)¨ R
doubleletter ← (∨/(2=/⊢))¨ R
substrings ← ∨⌿∨⌿¨ 'ab' 'cd' 'pq' 'xy' ∘.⍷ R

⎕ ← 'Part 1: ', +/ vowels ∧ doubleletter ∧ ~substrings

⍝ Create the following matrix for a following size
⍝  0 0 1 . 1 1 1
⍝  0 0 0 . 1 1 1
⍝  1 0 0 . 1 1 1
⍝  . . . . . . .
⍝  1 1 1 . 0 0 1
⍝  1 1 1 . 0 0 0
⍝  1 1 1 . 1 0 0
mask ← {(,⍨⍵)⍴ 1⌽3<⍳1+⍵}

hasTwoPair←{1∊(mask ¯1+⍴⍵)∧ ∘.≡⍨ 2,/⍵}
                                  ⍝ all pairs
                            ⍝ where pairs match
              ⍝ mask out identity and 'aaa'
            ⍝ at least one match

hasSandwich←{1∊({1=⍥(⌷∘⍵)3}⌺3)⍵}
                          ⍝ for each group of 3
                 ⍝ index 1 and 3
                  ⍝ are equal
             ⍝ at least one match

⎕← 'Part 2: ', +/(hasSandwich∧hasTwoPair)¨R
