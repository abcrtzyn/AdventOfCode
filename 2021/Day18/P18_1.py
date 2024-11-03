from snailfish import Snailfish, Pair

a = Snailfish(Pair(Pair(Pair(Pair(0,1),2),3),Pair(4,Pair(Pair(5,6),7))),[4,3,4,4,7,8,4,9])
b = Snailfish(Pair(0,1),[1,1])
n: Snailfish = a + b
n.attemptExplode()


# (((((0,1),2),3),(4,((5,6),7))),(8,9))
# [    4,3, 4, 4,  7,  8,4, 9,    1,1]
# explosion

# ((((   0 ,2),3),(4,((5,6),7))),(8,9))
# [     0,3, 7, 4,  7,  8,4, 9,    1,1]
# decrement following indicies
# ((((   0 ,1),2),(3,((4,5),6))),(7,8))
# [      0, 7, 4,  7,  8,4, 9,    1,1]


