input_file = r"~\input.txt"

with open(input_file, 'r') as file:
    numbers = file.read().split()

numbers = list(map(int, numbers))
print(numbers)