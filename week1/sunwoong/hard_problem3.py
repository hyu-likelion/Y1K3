word = list(input().lower())
words = [0 for i in range(26)]
largestNum = 0
largestChar = ''

for i in range(0, len(word)):
    index = ord(word[i])-97
    words[index] += 1
    if words[index] > largestNum:
        largestNum = words[index]
        largestChar = word[i]
    elif words[index] == largestNum:
        largestChar = '?'
    
print(largestChar.upper())