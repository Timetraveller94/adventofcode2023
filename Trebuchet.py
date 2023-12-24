file_path = "./input/input1.txt"
total_sum = 0

with open(file_path, "r") as file:
    for line in file:
        first_digit = None
        last_digit = None
        for i in range(len(line)):
            char = None
            if line[i].isdigit():
                char = line[i]
            else:
                substr = line[i:]
                if substr.startswith("one"): char = "1"
                elif substr.startswith("two"): char = "2"
                elif substr.startswith("three"): char = "3"
                elif substr.startswith("four"): char = "4"
                elif substr.startswith("five"): char = "5"
                elif substr.startswith("six"): char = "6"
                elif substr.startswith("seven"): char = "7"
                elif substr.startswith("eight"): char = "8"
                elif substr.startswith("nine"): char = "9"
            if char is not None:
                if first_digit is None:
                    first_digit = int(char)
                last_digit = int(char)
        two_digit_number = int(str(first_digit) + str(last_digit))
        total_sum += two_digit_number

print(total_sum)
