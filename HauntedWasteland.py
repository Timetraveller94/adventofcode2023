import re
import math

filepath = './input/HauntedWasteland.txt'
steps = ""
graph = {}

with open(filepath, 'r') as file:
    steps = file.readline().strip()
    print("stepsLen:", len(steps))
    file.readline()
    for line in file:
        match = re.search(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)', line)
        if match:
            key = match.group(1)
            value1 = match.group(2)
            value2 = match.group(3)
            graph[key] = [value1, value2]

def findLoops(vertex):
    visited = {}
    current = vertex
    stepIndex = 0
    count = 0
    isZin = False
    while current not in visited or stepIndex not in visited[current]:
        if not isZin: count += 1
        if current[2] == 'Z': isZin = True
        if current not in visited:
            visited[current] = set()
        visited[current].add(stepIndex)
        if steps[stepIndex] == 'L':
            current = graph[current][0]
        else:
            current = graph[current][1]
        stepIndex = (stepIndex + 1) % len(steps)
    # exit from a loop, find out the loop length and print the loop
    loopStart = current
    loopIndex = stepIndex
    loops = []
    while True:
        loops.append(current)
        if steps[stepIndex] == 'L':
            current = graph[current][0]
        else:
            current = graph[current][1]
        stepIndex = (stepIndex + 1) % len(steps)
        if current == loopStart and stepIndex == loopIndex:
            break
    print(count, len(loops), loops)

for node in graph:
    if node[2] == 'A':
        findLoops(node)

def lcm(a, b):
    gcd_result = math.gcd(a, b)
    lcm_result = (a * b) // gcd_result
    return lcm_result

loopLens = [11567, 21251, 12643, 16409, 19099, 14257]
result = 1
for i in loopLens:
    result = lcm(result, i)
print(result)