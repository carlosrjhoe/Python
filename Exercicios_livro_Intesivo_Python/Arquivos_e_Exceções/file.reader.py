file_name = "pi_digits.txt"

with open(file_name) as file:
    for line in file:
        print(line.strip())