filepath = "./input/GearRatios.txt"
graphs = []
numDict = []

with open(filepath, 'r') as file:
    for line in file:
        graphs.append(line.strip())
        left = right = 0
        curDict = {}
        while left < len(line):
            while left < len(line) and (not line[left].isdigit()):
                left += 1
            right = left + 1
            while right < len(line) and line[right].isdigit():
                right += 1
            if left >= len(line): break
            num = int(line[left:right])
            for i in range(left, right):
                curDict[i] = num
            left = right
        numDict.append(curDict)

total_gear = 0
for i, line in enumerate(graphs):
    for j, char in enumerate(line):
        total_num = 0
        total_power = 1
        if char == '*':
            if i > 0:
                if j in numDict[i-1]:
                    total_num += 1
                    total_power *= numDict[i-1][j]
                else:
                    if j > 0 and j-1 in numDict[i-1]:
                        total_num += 1
                        total_power *= numDict[i-1][j-1]
                    if j < len(line) - 1 and j+1 in numDict[i-1]:
                        total_num += 1
                        total_power *= numDict[i-1][j+1]
            if j > 0 and j-1 in numDict[i]:
                total_num += 1
                total_power *= numDict[i][j-1]
            if j < len(line) - 1 and j+1 in numDict[i]:
                total_num += 1
                total_power *= numDict[i][j+1]
            if i < len(graphs) - 1:
                if j in numDict[i+1]:
                    total_num += 1
                    total_power *= numDict[i+1][j]
                else:
                    if j > 0 and j-1 in numDict[i+1]:
                        total_num += 1
                        total_power *= numDict[i+1][j-1]
                    if j < len(line) - 1 and j+1 in numDict[i+1]:
                        total_num += 1
                        total_power *= numDict[i+1][j+1]
            if total_num == 2:
                total_gear += total_power
print(total_gear)