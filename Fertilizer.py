import re
filepath = "./input/Fertilizer.txt"
minLocation = None
seeds = []
seed_range = []
mappings = []

with open(filepath, 'r') as file:
    line = file.readline().strip()
    seeds_str = re.findall(r'\d+', line)
    seeds = list(map(int, seeds_str))
    for i in range(len(seeds)):
        if (i%2 == 1): continue
        seed_range.append([seeds[i], seeds[i]+seeds[i+1]])
    line = file.readline()
    for line in file:
        current_map = []
        for line in file:
            if line.isspace(): break
            current_map.append(list(map(int, line.strip().split(' '))))
        mappings.append(current_map)

for i in range(len(seed_range)):
    unmap = [seed_range[i]]
    mapped = []
    for mapping in mappings: 
        for record in mapping:
            new_unmap = []
            left = record[1] #inclusive
            right = record[1] + record[2] #exclusive
            for candidate in unmap:
                #candidate does not overlap with record
                if candidate[1] <= left or candidate[0] >= right:
                    new_unmap.append(candidate)
                #candidate is completely covered by record
                elif candidate[0] >= left and candidate[1] <= right:
                    new_candidate = [candidate[0] - left + record[0], candidate[1] - left + record[0]]
                    mapped.append(new_candidate)
                #record is completely covered by candidate
                elif candidate[0] <= left and candidate[1] >= right:
                    new_unmap.append([candidate[0], left])
                    new_unmap.append([right, candidate[1]])
                    mapped.append([record[0], right-left + record[0]])
                #candidate and record is overlapped to the right of the candidate
                elif candidate[0] < left and candidate[1] < right:
                    new_unmap.append([candidate[0], left])
                    mapped.append([record[0], candidate[1] - left + record[0]])
                #candidate and record is overlapped to the left of the candidate
                else:
                    new_unmap.append([right, candidate[1]])
                    mapped.append([candidate[0] - left + record[0], right - left + record[0]])
            unmap = new_unmap
        unmap = unmap+mapped
        mapped = []
    # Sort unmap based on the first element of each sub-array
    for candidate in unmap:
        if minLocation is None or candidate[0] < minLocation:
            print("update minLocation to:" + str(candidate[0]))
            minLocation = candidate[0]

print(minLocation)