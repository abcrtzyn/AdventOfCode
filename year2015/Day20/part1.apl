'factors' ⎕CY 'dfns'

key ← ⍎⊃⊃⎕NGET 'Day20/input.txt' 1

⍝ part 1, something like this is pretty good
⌊/⍸(key ÷ 10)≤(×/⍥(∪{((⍺*1+⍵)-1)÷(⍺-1)}¨⊢∘≢⌸)factors)¨ 831000+⍳1000

⍝ without factors

(36000000÷10)<= (+/∘∪⊢∨⍳) n
⍝ pretty slow, would be better to just check until found or just know the highest sum of divisors

⍝ for the next case, we get rid of factors below n/50 and sum the rest
