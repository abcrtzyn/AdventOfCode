⍝ largest numbers in ranges are 10 digits
⎕IO ← 0

file ← ⊃⊃⎕NGET 'Day02/input.txt' 1
regions ← 0 1∘+¨ ⍎¨¨('-'∘≠⊆⊢)¨(','∘≠⊆⊢)file
                              ⍝ split by comma
                    ⍝ for each split by dash
                 ⍝ parse the numbers
          ⍝ add 1 to ending index for inclusiveness

⍝ this gets all 2 digit
⍝ 11× 1+⍳9
⍝ this gets all 4 digit
⍝ 101× 10+⍳90
⍝ creates a list of all invalid IDs given a length, only even numbers are allowed
⍝ generalized version of the above examples
invalid_1 ← {{(1+10×⍵)×⍵+⍳9×⍵}(10÷⍨10*⍵÷2)}

⎕PP ← 14
⍝ there are only 99999 invalid IDs for part 1, I can check all at once
⍝ by using 5 seperate lists, interval index can shortcut a lot and in runs very fast
⎕ ← 'Part 1: ', +/+/¨{(∨⌿ 0 = regions ∘.⍸ ⍵)/¨⍵} invalid_1¨ 2 4 6 8 10
                                                 ⍝ creates 5 lists of invalid ids 
                                      ⍝ find where they fall on each region using interval index
                          ⍝ within the region if = 0
                       ⍝ fold to get a boolean for each potenital invalid id
                                            ⍝ select only those that are within range
                ⍝ sum them 





⍝ possible part 2 combinations
⍝            length 2 3 4 5 6 7 8 9 10
⍝ 1 digit  repeated 2 3 4 5 6 7 8 9 10 times
⍝ 2 digits repeated     2   3   4    5 times
⍝ 3 digits repeated         2     3    times
⍝ 4 digits repeated             2      times
⍝ 5 digits repeated                  2 times
⍝ duplicates are in here

⍝ 11 111 1111 11111 111111 1111111 11111111 111111111 1111111111
⍝ 101 10101 1010101 101010101
⍝ 1001 1001001
⍝ 10001
⍝ 100001

⍝ this takes in a number of digits to repeat ⍵ and a multiplier ⍺, produces a list of numbers
invalid_2 ← {⍺{⍺ × ⍵+⍳9×⍵}10*¯1+⍵}

list_2 ← {
    l1←invalid_2∘1 ¨ 9÷⍨¯1+10* 2+ ⍳ 9  ⍝ this is the sequence 1 11 111 ...
    l2←invalid_2∘2 ¨ 99÷⍨¯1+100* 2+ ⍳ 4
    l3←invalid_2∘3 ¨(1001 1001001)
    l4←invalid_2∘4 ¨(10001)
    l5←invalid_2∘5 ¨(100001)
    l1 , l2 , l3 , l4 , l5
}


⎕ ← 'Part 2: ', +/∪⊃,/{(∨⌿ 0 = regions ∘.⍸ ⍵)/¨⍵} list_2 1
                                                  ⍝ make the list of lists
                      ⍝ same as part 1, find which ids are in the ranges and select them
                    ⍝ ravel them all into one list
                  ⍝ take unique elements, removes duplicates
                ⍝ sum
