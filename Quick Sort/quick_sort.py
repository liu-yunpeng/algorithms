def ChoosePivot(array,flag):
	length = len(array)
	if length % 2 == 0:
		middle = length // 2
	else:
		middle = length // 2 + 1

	# ways to choose pivot: at start, at middle, at end, or median of the 3

	median_of_three = [array[0], array[middle], array[-1]].sort()[1]

	if flag == 1:
		return 0
	if flag == 2:
		return -1
	if flag == 3:
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


def QuickSort(array, flag):
	length = len(array)

	if length ==1:
		return array, 0
	else:
		pivot = ChoosePivot(array,flag)
		# swap pivot to the start of the array
		array = Swap(array, 0, pivot)