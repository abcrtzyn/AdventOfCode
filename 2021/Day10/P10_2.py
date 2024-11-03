matchChars = {'(':')','[':']','{':'}','<':'>'}

pointsDict = {')':1, ']':2, '}':3,'>':4}
scores = list()
with open('input.txt','r') as f:
    for line in f:
        chunkStack = list()
        for char in line:
            if char == '\n':
                lineScore = 0
                while len(chunkStack) != 0:
                    openChar = chunkStack.pop()
                    lineScore *= 5
                    lineScore += pointsDict[matchChars[openChar]]
                scores.append(lineScore)
            elif char in matchChars:
                chunkStack.append(char)
            else:
                openChar = chunkStack.pop()
                if matchChars[openChar] != char:
                    break
#print(scores)
print(sorted(scores)[len(scores)//2])
            