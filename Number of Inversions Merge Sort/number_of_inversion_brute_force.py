input_file = r"~\input.txt"

with open(input_file, 'r') as file:
    numbers = file.read().split()


numbers = list(map(int, numbers))
#print(numbers)


#numbers = [1,5,3,4,2,6]
#numbers = [1,2,3,5,4,6]
#numbers = [ 99888, 99889, 9989, 99890, 99891, 99892, 99893, 99894, 99895, 99896, 99897, 99898, 99899, 999, 9990, 99900]

count = 0

for i in numbers:
    for j in range(i, len(numbers)):
        if numbers[i] > numbers[j]:
            count += 1

            #if count % 10000 == 0:
            if count % 1000000 == 0:
                print('processsed', count)

print(count)