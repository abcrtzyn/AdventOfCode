matchChars = {'(':')','[':']','{':'}','<':'>'}

pointsDict = {')':3, ']':57, '}':1197,'>':25137}
score = 0
with open('input.txt','r') as f:
    for line in f:
        chunkStack = list()
        for char in line:
            if char == '\n':
                break #ignore line
            elif char in matchChars:
                chunkStack.append(char)
            else:
                openChar = chunkStack.pop()
                if matchChars[openChar] != char:
                    score += pointsDict[char]
                    break
print(score)
            