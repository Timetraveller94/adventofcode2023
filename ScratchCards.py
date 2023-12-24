import re
filepath = "./input/ScratchCards.txt"
total_point = 0

"""
with open(filepath, 'r') as file:
    for line in file:
        games = line.strip().split(':')
        numbers = games[1].split('|')
        winning_number = re.findall(r'\d+', numbers[0])
        winning_number_dict = {int(num): None for num in winning_number}
        my_number = re.findall(r'\d+', numbers[1])
        my_number = list(map(int, my_number))
        cur = 0
        for num in my_number:
            if num in winning_number_dict:
                if cur == 0: cur = 1
                else: cur *= 2
        total_point += cur
"""

count = []
winning_number = []
my_number = []
with open(filepath, 'r') as file:
    for line in file:
        count.append(1)
        games = line.strip().split(':')
        numbers = games[1].split('|')
        winning = re.findall(r'\d+', numbers[0])
        winning_number.append({int(num): None for num in winning})
        my = re.findall(r'\d+', numbers[1])
        my_number.append(list(map(int, my)))
for i in range(len(my_number)):
    cur_win = 0
    for num in my_number[i]:
        if num in winning_number[i]:
            cur_win += 1
    for j in range(cur_win):
        count[i+1+j] += count[i]

total_point = sum(count)
print(total_point)
        