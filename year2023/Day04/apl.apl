
R←⊃⎕NGET 'Day04/input.txt' 1

⍝ parse the file, remove 'Card n:' and split by the |
data←{↑⍎¨¨(('|'≠⊢)⊆⊢)¨9↓¨⍵} R
⍝ the number of matches per card
matches←+/↑∊/data
           ⍝ are the winning numbers there
        ⍝ count matches

⎕←'Part 1: ',+/⌊2*1-⍨ matches
                ⍝ 2^(1-matches) gives score
                ⍝ 2^¯1 = 0.5 → 0
             ⍝ sum all cards 


⍝ part 2
⍝ this solution was found and reworked

⍝ given a matrix that shows how many cards are copied
⍝ repeated multiplication of this matrix will give a total number cards


⍝            1  2  3  4  5  6
⍝      
⍝ null    1  1  1  1  1  1  1  ⍝ the null card keeps the recursion in check
⍝ card 1  0  0  1  1  1  1  0  ⍝ cards are not creating copies of themselves
⍝ card 2  0  0  0  1  1  0  0
⍝ card 3  0  0  0  0  1  1  0
⍝ card 4  0  0  0  0  0  1  0
⍝ card 5  0  0  0  0  0  0  0
⍝ card 6  0  0  0  0  0  0  0


⍝ produces intervals for each card
intervals ← {(⊂1, 2+⍴⍵),2+(⍳⍴⍵)+0,¨⍵}matches
⍝             (1 8)        (i i+match)

⍝ generates the matrix above from the intervals
gen ← {⍉1=↑⍸∘(⍳⍴⍵)¨⍵} intervals
        ⍝ make binary masks using interval index


⎕←'Part 2: ', ¯1++/(gen∘(+.×)⍣≡) 1,(≢matches)/0
                                 ⍝ start it off with 1 null card
                    ⍝ continue multiplying by the generator until
                    ⍝ the result doesn't change (at most ≢matches times)
                 ⍝ sum the cards
             ⍝ subtract the intial null card
