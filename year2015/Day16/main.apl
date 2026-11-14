⍝ INCOMPLETE SOLUTION

keys ← 'children' 'cats' 'samoyeds' 'pomeranians' 'akitas' 'vizslas' 'goldfish' 'trees' 'cars' 'perfumes'
values ← 3 7 2 3 0 0 5 3 2 1

⍝ this is a list of key value pairs
kv1 ← ↓⍉↑ keys values


R ← ' ,:'∘(~⍤∊⍨⊆⊢)¨ ⊃ ⎕NGET 'Day16/input.txt' 1
    ⍝ split up into words


⍝ in this case, sues is just ⍳500, but it is here for completeness
⍝ if your sues happened to be out of order in the input, my code would handle it
sues ← ⍎¨ 2⊃¨ R
          ⍝ just take the sue index for each line
       ⍝ turn each into a numbr

parsed ← ↓¨ ((⍎¨@2⍤1) 3 2 ⍴ ⊢)¨ 2↓¨ R
                               ⍝ drop the Sue x
                              ⍝ for each line
                     ⍝ reshape to a table
              ⍝ eval the numbers (in the second column)
         ⍝ turn each into a list of key value pairs
⍝ parsed is a list of list key value pairs



⎕←'Part 1: ', (3=kv1∘(+/⍤,∘.≡)¨parsed) / sues
                              ⍝ for each sue
                          ⍝ for each kv pair in expected and sue
                          ⍝ make sure the kv pairs match
                      ⍝ ravel and sum, this is the number of correct traits for that sue
               ⍝ the one with three correct traits is the answer
                                       ⍝ get the index of that sue


⍝ part 2 requires doing different comparisons on each trait
⍝ can not just check if the keys and value match
⍝ we have to check that the keys match and the values fit the required comparison

⍝ ¯1 is less than, 1 is greater than, 0 is equal
operator2 ← 0 1 0 ¯1 0 0 ¯1 1 0 0
kv2 ← ↓⍉↑ keys operator2 values

⍝ this takes in a key, op, value expected with a key value from a sue
⍝ and returns if the keys match and the values are correct
part2 ← {
    ⍺[1]≢⍵[1]: 0 ⍝ if the keys don't match, instant 0
    ⍺[2]=¯1: (⍺[3]>⍵[2])
    ⍺[2]=0:  (⍺[3]=⍵[2])
    ⍺[2]=1:  (⍺[3]<⍵[2])
}

⍝ exact same as part 1 just with part2 function rather than ≡
⎕←'Part 2: ', (3=kv2∘(+/⍤,∘.part2)¨parsed) / sues
