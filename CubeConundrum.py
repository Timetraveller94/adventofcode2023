import re
setting = [12, 13, 14]
filepath = "./input/CubeConundrum.txt"
total_sum = 0
total_power = 0
with open(filepath, 'r') as file:
    for line in file:
        substrings = line.strip().split(':')
        # Check if substrings[0] matches the pattern "Game %n"
        match = re.match(r"Game (\d+)", substrings[0])
        if match:
            # Fetch the number and store it in a variable
            game_number = int(match.group(1))
            print("Game Number:", game_number)
        steps = substrings[1].split(';')
        feasible = True
        red, green, blue = 0, 0, 0
        for step in steps:
            match = re.search(r"(\d+) red", step)
            if match:
                red = max(red, int(match.group(1)))
            match = re.search(r"(\d+) green", step)
            if match:
                green = max(green, int(match.group(1)))
            match = re.search(r"(\d+) blue", step)
            if match:
                blue = max(blue, int(match.group(1)))
        total_power += red * green * blue

print(total_power)