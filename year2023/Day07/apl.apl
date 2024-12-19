⎕IO ← 0

R←⊃⎕NGET 'Day07/input.txt' 1


bids←⍎¨1⌷[1]↑(' '∘≠⊆⊢)¨R
hands←0⌷[1]↑(' '∘≠⊆⊢)¨R

⍝ part 1

⍝ gives the cards for each hand as numbers [0,13)
cards←('23456789TJQKA'∘⍳)
⍝ cards¨hands

⍝ shows number 5, 4, 3, 2 of a kinds that are ordered for hand scores
type←(+/5 4 3 2∘.=∘(+/)'23456789TJQKA'∘.=⊢)
⍝ type¨hands

⎕←'Part 1: ', +/bids×1+⍋⍋2 2 2 3 13 13 13 13 13∘⊥¨(type,cards)¨hands
                                    ⍝ decode (hand type, hand card)
                       ⍝ rank the hands
                    ⍝ multiply bids


⍝ part 2
⍝ gives the cards for each hand as numbers [0,13)
cards←('J23456789TQKA'∘⍳)
⍝ cards¨hands

⍝ this table converts (#J, #5ofk, #4ofk, #3ofk, #2ofk) into the hand type 0: high card, 1: one pair, 2: two pair, 3: three kind, 4: full house, 5: four kind, 6: five kind
lookup ← 6 2 2 2 3 ⍴ 0 1 2 3 4 0 5 0 0 0 0 0 6 0 0 0 0 0 0 0 0 0 0 0  1 3 4 5 5 0 6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  3 5 5 6 6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  5 6 6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

⍝ this is a method that is more suited to array programming, but I like the functional foreach better
⍝ {lookup⌷⍨⊆⍉(+/'J'=⍵),+/5 4 3 2(∘.=⍤1)+/'23456789TQKA'(∘.=⍤1)⍵}↑hands

⍝ shows number 5, 4, 3, 2 of a kinds that are ordered for hand scores
type←{lookup⌷⍨(+/'J'=⍵),+/5 4 3 2∘.=+/'23456789TQKA'∘.=⍵}
⍝ type¨hands

⎕←'Part 2: ', +/bids×1+⍋⍋7 13 13 13 13 13∘⊥¨(type,cards)¨hands
