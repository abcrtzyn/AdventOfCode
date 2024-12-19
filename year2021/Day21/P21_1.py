playerPos = [9,3]
playerScore = [0,0]
diceRolls = 0
dicePos = 100
currentPlayer = 0

def modifiedMod(n, m):
    return ((n-1) % m) + 1

def rollDice():
    global dicePos
    global diceRolls
    dicePos+=1
    dicePos = modifiedMod(dicePos, 100)
    diceRolls += 1
    return dicePos

while True:
    diceSum = rollDice() + rollDice() + rollDice()
    playerPos[currentPlayer] += diceSum
    playerPos[currentPlayer] = modifiedMod(playerPos[currentPlayer], 10)
    playerScore[currentPlayer] += playerPos[currentPlayer]
    if playerScore[currentPlayer] >= 1000:
        print(playerScore[(currentPlayer+1)%2] * diceRolls)
        break
    currentPlayer += 1
    currentPlayer = currentPlayer % 2
