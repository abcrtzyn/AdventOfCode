from dataclasses import dataclass
from typing import List

diceOptions = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]
playerWins = [0,0]
@dataclass
class Context:
    playerPos: List[int]
    playerScore: List[int]
    currentPlayer: bool
    universeMultiplier: int

contexts: List[Context] = []
contexts.append(Context([9,3], [0,0], False, 1))


def modifiedMod(n, m):
    return ((n-1) % m) + 1

while len(contexts) != 0:
    context = contexts.pop()
    for roll, multiplier in diceOptions:
        playerPos = context.playerPos.copy()
        playerScore = context.playerScore.copy()
        currentPlayer = context.currentPlayer
        universeMultiplier = context.universeMultiplier

        playerPos[currentPlayer] += roll
        playerPos[currentPlayer] = modifiedMod(playerPos[currentPlayer], 10)
        playerScore[currentPlayer] += playerPos[currentPlayer]
        if playerScore[currentPlayer] >= 21:
            playerWins[currentPlayer] += universeMultiplier * multiplier
            continue        
        contexts.append(Context(playerPos, playerScore, not currentPlayer, universeMultiplier * multiplier))
    #print(len(contexts), end=' ')
print(playerWins)