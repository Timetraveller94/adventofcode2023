import math
filepath = './input/MirageMaintenance.txt'

combinations_dict = []
history = []

with open(filepath, 'r') as file:
    for line in file:
        integers = [int(num) for num in line.split()]
        reverse(integers)
        history.append(integers)
        
def calculate_combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

for i in range(0, 22):
    cache = []
    for j in range(0, i + 1):
        cache.append(calculate_combinations(i, j))
    combinations_dict.append(cache)

total = 0
for game in history:
    cur = 0
    for i in range(0, len(game)):
        for j in range(0, i + 1):
            cur += pow(-1, i - j) * combinations_dict[i][i-j] * game[len(game) - 1 + j - i]
    total += cur

print(total)