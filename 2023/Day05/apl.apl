⍝ this one seems easy to do in a array language
⍝ but memory usage is a problem (if converting the maps)
⍝ and it is harder than I thought to handle ranges, especially doing math with ranges


⍝ R←⊃⎕NGET 'Day05/test_input.txt' 1

⍝ seeds←⍎6↓⊃R
⍝ maps←↑¨⍎¨¨1∘↓¨((⊃0∘≠∘⍴)¨⊆⊢)2↓R

⍝ ⍝ given a map and a number
⍝ ⍝ the mapped number is 




⍝ ⍝ ⍺ is a map
⍝ ⍝ ⍵ is a list of seeds
⍝ mapsingle ← {
⍝       offset←⍵-(2⊃⍺)
⍝       onlyif←(1⊃⍺)+offset
⍝       condition←(0≤offset) ∧ (offset < (2⊃⍺)+(3⊃⍺))
      
⍝ }
