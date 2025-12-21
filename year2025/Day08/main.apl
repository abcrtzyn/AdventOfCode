⍝ strongly connected components and binary search from dfns
'scc' 'bsearch' ⎕CY'dfns'

file ← ⍎¨¨(','∘≠⊆⊢)¨⊃⎕NGET 'Day08/input.txt' 1
⍝ number_of_connections ← 10 ⍝ for the testing input
number_of_connections ← 1000 ⍝ for the real input

⍝ from APLcart with modifications
⍝ I am very unfamiliar with the rank operator thus don't fully understand how this works
euclidian_squared ← (1⊥2*⍨-)⍤1⍤1 2⍨
                                  ⍝ selfie
                            ⍝ rank op magic
                       ⍝ square and subtract
                    ⍝ plus reduce (unary decode)

⍝ checking for unique distances
⍝ if these numbers match, all distances between points are unique
⍝ ⎕←1++/⍳¯1+≢ file
⍝ ⎕←≢∪, euclidian_squared ↑ file

⍝ number of points in the file to use for reshape later
SIZE ← ≢ file

⍝ this is my ranking cutoff, so any rank above this is not an edge
cutoff ← SIZE + 2×number_of_connections
⍝ edges included are each vertex to itself, and [number of connections] A to B and B to A, hence ×2

dist_ranks ← SIZE SIZE ⍴⍋⍋, euclidian_squared ↑ file
                                              ⍝ turn into a table
                            ⍝ get distances
                          ⍝ ravel into a list
                        ⍝ rank all the distances
                       ⍝ reshape back to the grid

graph ← {{⍵/⍳⍴⍵}¨↓⍵} cutoff≥ dist_ranks
                     ⍝ connect only those below the cutoff
        ⍝ turn adjacency mat into vector form (dfns.Graphs)
                    

⎕←'Part 1: ', ×/3↑(⊂∘⍒⌷⊢) {≢⍵}⌸ scc graph
                                ⍝ find the strongly connected components
                          ⍝ how many verticies in each component
                  ⍝ sort
                ⍝ grab top 3
              ⍝ multiply

⍝ part 2 going to do a binary search to find the lowest number of connections to get one connected component.
part2 ← {
    cutoff ← SIZE + 2×⍵
    graph ← {{⍵/⍳⍴⍵}¨↓⍵} cutoff≥ dist_ranks
    1=≢∪ scc graph
}


⍝ this gives the amount of connections needed
single_connections ← part2 bsearch 1 (+/⍳¯1+≢ file)
                          ⍝ binary search part2 in range 1 through all possible connections
⍝ convert that to a cutoff value
single_cutoff ← SIZE + 2×single_connections

⍝ using the number found, figure out which two nodes get connected
⎕←'Part 2: ', ×/⊃¨file[SIZE {1 0 + 0 ⍺⊤⍵} ⊃single_cutoff ⍳⍨, dist_ranks]
                                           ⍝ find where this appears in the distance matrix
                            ⍝ divide and mod by SIZE (gives row and column of that cutoff value)
                  ⍝ index into file to get the two points
                ⍝ get the X coords
              ⍝ multiply
