from queue import Queue
filepath = './input/PipeMaze.txt'
inputGraph = []
with open(filepath, 'r') as file:
    for line in file:
        row = line.strip()
        inputGraph.append(row)

graph = [['.'] * (len(inputGraph[0]) + 2) for _ in range(len(inputGraph) + 2)]
distance = [[-1] * len(graph[0]) for _ in range(len(graph))]

s = []
for i in range(len(inputGraph)):
    for j in range(len(inputGraph[0])):
        graph[i + 1][j + 1] = inputGraph[i][j]
        if 'S' == graph[i + 1][j + 1]:
            s = [i + 1, j + 1]
            graph[i+1][j+1] = 'J'
            distance[i+1][j+1] = 0

# find the loop
queue = Queue()
queue.put(s)
lx = len(graph)
ly = len(graph[0])

while not queue.empty():
    cur = queue.get()
    x, y = cur[0], cur[1]
    if graph[x][y] == '|':
        if distance[x+1][y] == -1:
            queue.put([x+1, y])
            distance[x+1][y] = distance[x][y] + 1
        if distance[x-1][y] == -1:
            queue.put([x-1, y])
            distance[x-1][y] = distance[x][y] + 1
    elif graph[x][y] == '-':
        if distance[x][y+1] == -1:
            queue.put([x, y+1])
            distance[x][y+1] = distance[x][y] + 1
        if distance[x][y-1] == -1:
            queue.put([x, y-1])
            distance[x][y-1] = distance[x][y] + 1
    elif graph[x][y] == 'L':
        if distance[x-1][y] == -1:
            queue.put([x-1, y])
            distance[x-1][y] = distance[x][y] + 1
        if distance[x][y+1] == -1:
            queue.put([x, y+1])
            distance[x][y+1] = distance[x][y] + 1
    elif graph[x][y] == 'J':
        if distance[x-1][y] == -1:
            queue.put([x-1, y])
            distance[x-1][y] = distance[x][y] + 1
        if distance[x][y-1] == -1:
            queue.put([x, y-1])
            distance[x][y-1] = distance[x][y] + 1
    elif graph[x][y] == '7':
        if distance[x][y-1] == -1:
            queue.put([x, y-1])
            distance[x][y-1] = distance[x][y] + 1
        if distance[x+1][y] == -1:
            queue.put([x+1, y])
            distance[x+1][y] = distance[x][y] + 1
    elif graph[x][y] == 'F':
        if distance[x][y+1] == -1:
            queue.put([x, y+1])
            distance[x][y+1] = distance[x][y] + 1
        if distance[x+1][y] == -1:
            queue.put([x+1, y])
            distance[x+1][y] = distance[x][y] + 1

# Part 1: Find the largest number in the distance array
#largest_distance = max(max(distance, key=max))
#print("Largest distance:", largest_distance)

# Part 2: Find the inner part of the loop: hint, always fill the right/left side of your loop
# then you're able to distinguish the inner/outer area of your loop
# I'll take the right here.
x = s[0]
y = s[1]
direction = 'right'
while True:
    if direction == 'up':
        if graph[x][y] == 'F':
            direction = 'right'
            y += 1
        elif graph[x][y] == '7':
            direction = 'left'
            if distance[x][y+1] == -1:
                distance[x][y+1] = -2
            if distance[x-1][y] == -1:
                distance[x-1][y] = -2            
            y -= 1
        elif graph[x][y] == '|':
            if distance[x][y+1] == -1:
                distance[x][y+1] = -2
            x -= 1
    elif direction == 'down':
        if graph[x][y] == 'L':
            direction = 'right'
            if distance[x][y-1] == -1:
                distance[x][y-1] = -2
            if distance[x+1][y] == -1:
                distance[x+1][y] = -2
            y += 1
        elif graph[x][y] == 'J':
            direction = 'left'
            y -= 1
        elif graph[x][y] == '|':
            if distance[x][y-1] == -1:
                distance[x][y-1] = -2
            x += 1
    elif direction == 'right':
        if graph[x][y] == 'J':
            direction = 'up'
            if distance[x][y+1] == -1:
                distance[x][y+1] = -2
            if distance[x+1][y] == -1:
                distance[x+1][y] = -2
            x -= 1
        elif graph[x][y] == '7':
            direction = 'down'
            x += 1
        elif graph[x][y] == '-':
            if distance[x+1][y] == -1:
                distance[x+1][y] = -2
            y += 1
    elif direction == 'left':
        if graph[x][y] == 'L':
            direction = 'up'
            x -= 1
        elif graph[x][y] == 'F':
            direction = 'down'
            if distance[x][y-1] == -1:
                distance[x][y-1] = -2
            if distance[x-1][y] == -1:
                distance[x-1][y] = -2
            x += 1
        elif graph[x][y] == '-':
            if distance[x-1][y] == -1:
                distance[x-1][y] = -2
            y -= 1
    if x == s[0] and y == s[1]: break

# for everything marked as -2, flood fill its neighbour
queue = Queue()
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if distance[i][j] == -2:
            queue.put([i, j])
lx = len(graph)
ly = len(graph[0])

while not queue.empty():
    cur = queue.get()
    x, y = cur[0], cur[1]
    if y - 1 >= 0 and distance[x][y-1] == -1:
        queue.put([x, y-1])
        distance[x][y-1] = -2
    if y + 1 < ly and distance[x][y+1] == -1:
        queue.put([x, y+1])
        distance[x][y+1] = -2
    if x-1 >= 0 and distance[x-1][y] == -1:
        queue.put([x-1, y])
        distance[x-1][y] = -2
    if x+1 < ly and distance[x+1][y] == -1:
        queue.put([x+1, y])
        distance[x+1][y] = -2


result = 0
loopLen = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if distance[i][j] == -2:
            result += 1
        elif distance[i][j] >= 0:
            loopLen += 1

print(distance)
print(result, loopLen, len(graph) * len(graph[0]) - loopLen - result)