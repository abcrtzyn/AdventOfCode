R←⊃⎕NGET 'Day05\input.txt' 1
has3vowels←{+/'aeiou'∘.=}
hasDoubleLetter←{∨/2=/⍵}
hasStrings←{∨/∨/[1]↑(⍵)∘(⍷⍨)¨⍺}
+/{(hasDoubleLetter ⍵)∧(has3vowels ⍵)∧~('ab' 'cd' 'pq' 'xy')∘hasStrings ⍵}↑R ⍝ part 1

HasTwoPair←{∨/∨/((2∘<∧(⍴⍵)∘>)((¯1+⍴⍵)[1 1])⍴⍳(⍴⍵))∧(⊢∘.≡⊢)2,/⍵}
HasSandwich←{∨/({=/⍵[1 3]}⌺3)⍵}
+/(HasSandwich∧HasTwoPair)¨R ⍝ part 2