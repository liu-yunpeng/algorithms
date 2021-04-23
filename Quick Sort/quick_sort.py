input_file = r"~\input.txt"

with open(input_file, 'r') as f:
    input_data = [int(x) for x in f]


def ChoosePivot(array):
    n = len(array)
    if int(n/2)*2==n:
        middle = n//2 - 1
    elif int(n/2)*2<n:
        middle = n//2
        
    
    temp_array = [array[0], array[middle], array[-1]]
    temp_array.sort()
    median_of_three = temp_array[1]
    if array[0] ==  median_of_three:
        return 0
    if array[middle] == median_of_three:
        return middle
    if array[-1] == median_of_three:
        return -1

def Swap(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1] 
    return array

def Partition(array):
    pivot = array[0]
    length = len(array)
    pos_pointer = 1

    for i in range(1,length):
        if array[i] < pivot:
            array = Swap(array, pos_pointer, i)
            pos_pointer += 1
    array = Swap(array,0 , pos_pointer - 1)
    return array, pos_pointer - 1
    
def QuickSort(array):
    n = len(array)
    
    if n>1:
        p = ChoosePivot(array)
        array = Swap(array,0,p)
        array,pivot_position = Partition(array)
        array[:pivot_position] = QuickSort(array[:pivot_position])
        array[pivot_position+1:] = QuickSort(array[pivot_position+1:])
        
        return array
    else:
        return array





#print(input_data)


print(QuickSort(input_data))
