input_file = r"~\input.txt"

with open(input_file, 'r') as file:
    numbers = file.read().split()

numbers = list(map(int, numbers))
print(numbers)


#numbers = [1,2,3,5,4,6]
#numbers = [ 99888, 99889, 9989, 99890, 99891, 99892, 99893, 99894, 99895, 99896, 99897, 99898, 99899, 999, 9990, 99900]


def GetInversion(lst):
    if len(lst) == 1:
        return [lst, 0]

    
    left = lst[:len(lst) // 2]
    right = lst[len(lst) // 2:]
    
    left_sorted, left_inversions = GetInversion(left)
    right_sorted, right_inversions = GetInversion(right)
    
    # merge left and right
    i = 0    # index to iterate through left and right
    j = 0    # index to iterate through left and right
    split_inversions = 0
    sorted_array = []
    
    counter = 0
    
    while i < len(left_sorted) and j < len(right_sorted) and counter < 30:
        if left_sorted[i] > right_sorted[j]:
            split_inversions += (len(left_sorted) - i)
            sorted_array.append(right_sorted[j])
            j += 1
        else:
            sorted_array.append(left_sorted[i])
            i += 1
            
        counter += 1

    if i < len(left_sorted):
        sorted_array.extend(left_sorted[i:])
    if j < len(right_sorted):
        sorted_array.extend(right_sorted[j:])
    
    #print(left)
    #print(right)

    total_inversions = left_inversions + right_inversions + split_inversions

    return [sorted_array, total_inversions]
    

print(GetInversion(numbers))