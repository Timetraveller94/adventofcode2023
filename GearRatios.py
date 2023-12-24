filepath = "./input/GearRatios.txt"
graphs = []

with open(filepath, 'r') as file:
    for line in file:
        graphs.append(line.strip())

total_num = 0
for index, line in enumerate(graphs):
    left, right = 0, 0
    # Rest of your code here
    while left < len(line):
        while left < len(line) and (not line[left].isdigit()):
            left += 1
        right = left + 1
        while right < len(line) and line[right].isdigit():
            right += 1
        #print(index, left, right)
        if left >= len(line): break
        num = int(line[left:right])
        count = False
        if index > 0:
            for i in range(left, right):
                if graphs[index-1][i] != '.' and (not graphs[index-1][i].isdigit()):
                    count = True
                    break
        if (not count) and index < len(graphs) - 1:
            for i in range(left, right):
                if graphs[index+1][i] != '.' and (not graphs[index+1][i].isdigit()):
                    count = True
                    break
        if (not count) and left > 0:
            if index > 0 and (graphs[index-1][left-1] != '.' and (not graphs[index-1][left-1].isdigit())):
                count = True
            if graphs[index][left-1] != '.' and (not graphs[index][left-1].isdigit()):
                count = True
            if index < len(graphs) - 1 and (graphs[index+1][left-1] != '.' and (not graphs[index+1][left-1].isdigit())):
                count = True
        if (not count) and right < len(line):
            if index > 0 and (graphs[index-1][right] != '.' and (not graphs[index-1][right].isdigit())):
                count = True
            if graphs[index][right] != '.' and (not graphs[index][right].isdigit()):
                count = True
            if index < len(graphs) - 1 and (graphs[index+1][right] != '.' and (not graphs[index+1][right].isdigit())):
                count = True
        if count:
            total_num += num
        left = right

print(total_num)