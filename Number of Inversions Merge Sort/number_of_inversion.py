input_file = r"~\input.txt"

with open(input_file, 'r') as file:
    numbers = file.read().split()

numbers = list(map(int, numbers))
print(numbers)


#numbers = [1,2,3,5,4,6]
#numbers = [ 99888, 99889, 9989, 99890, 99891, 99892, 99893, 99894, 99895, 99896, 99897, 99898, 99899, 999, 9990, 99900]