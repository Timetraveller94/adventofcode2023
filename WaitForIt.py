filepath = "./input/WaitForIt.txt"
total_value = 1
time = []
distance = []
import re
import math
with open(filepath, 'r') as file:
    line = file.readline().strip()    
    time = list(map(int, re.findall(r'\d+', line)))
    line = file.readline().strip()
    distance = list(map(int, re.findall(r'\d+', line)))

"""
for i in range(len(time)):
    xcount = 0
    for hold in range(time[i]):
        if hold * (time[i] - hold) > distance[i]:
            xcount += 1
    total_value *= xcount
"""

actual_time = 0
actual_distance = 0
time.reverse()
distance.reverse()
for t in time:
    actual_time = actual_time + pow(10, len(str(actual_time))) * t 
for d in distance:
    actual_distance = actual_distance + pow(10, len(str(actual_distance))) * d
actual_distance /= 10
actual_time /= 10
print(2 * math.sqrt(actual_time * actual_time / 4 - actual_distance))
