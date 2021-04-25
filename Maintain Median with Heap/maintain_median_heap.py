# -*- coding: utf-8 -*-
"""
@author: Yunpeng Liu
"""


input_file = r"~\input.txt"


with open(input_file, 'r') as f:
    input_data = []
    for line in f:
        input_data.append(int(line))
        
        
#input_data = input_data[:10]
print(input_data)


class Heap(object):
    def __init__(self, array = []):
        self.array = array
        
    def insert(self, value):
        pass
    
    
class Min_Heap(Heap):
    def __init__(self, array):
        super().__init__(array)
        
    def insert(self, value):
        self.array.append(value) 
        pos = len(self.array) - 1
        while pos != 0:
            parent_pos = int((pos - 1) / 2)
            if self.array[pos] < self.array[parent_pos]:
                self.array[pos], self.array[parent_pos] = self.array[parent_pos], self.array[pos]
            pos = parent_pos
            
        return self.array
    
    def pop(self):
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        min_value = self.array.pop() 
        pos = 0
        while pos * 2 + 2 < len(self.array):
            left = pos * 2 + 1
            right = pos * 2 + 2
            if self.array[left] < self.array[right]:
                
                if self.array[pos] > self.array[left]:
                    self.array[pos], self.array[left] = self.array[left], self.array[pos]
                    pos = left
                else:
                    break
            else:
                if self.array[pos] > self.array[right]:
                    self.array[pos], self.array[right] = self.array[right], self.array[pos]
                    pos = right
                else:
                    break
        
        # handle single left        
        if pos * 2 + 1 < len(self.array):
            left = pos * 2 + 1
            if self.array[pos] > self.array[left]:
                self.array[pos], self.array[left] = self.array[left], self.array[pos]
                pos = left
        
        return min_value
    
class Max_Heap(Heap):
    def __init__(self, array):
        super().__init__(array)
        
    def insert(self, value):
        self.array.append(value) 
        pos = len(self.array) - 1
        while pos != 0:
            parent_pos = int((pos - 1) / 2)
            if self.array[pos] > self.array[parent_pos]:
                self.array[pos], self.array[parent_pos] = self.array[parent_pos], self.array[pos]
            pos = parent_pos
            
        return self.array
    
    def pop(self):
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        max_value = self.array.pop() 
        pos = 0
        while pos * 2 + 2 < len(self.array):
            left = pos * 2 + 1
            right = pos * 2 + 2
            if self.array[left] > self.array[right]:
                
                if self.array[pos] < self.array[left]:
                    self.array[pos], self.array[left] = self.array[left], self.array[pos]
                    pos = left
                else:
                    break
            else:
                if self.array[pos] < self.array[right]:
                    self.array[pos], self.array[right] = self.array[right], self.array[pos]
                    pos = right
                else:
                    break
        
        # handle single left        
        if pos * 2 + 1 < len(self.array):
            left = pos * 2 + 1
            if self.array[pos] < self.array[left]:
                self.array[pos], self.array[left] = self.array[left], self.array[pos]
                pos = left
        
        return max_value
  
'''
h1 = Min_Heap([])
h1.insert(4)
h1.insert(12)
h1.insert(5)
h1.insert(7)
h1.insert(21)
h1.insert(2)
h1.insert(11)
print(h1.array)

h2 = Max_Heap([])
h2.insert(4)
h2.insert(12)
h2.insert(5)
h2.insert(7)
h2.insert(21)
h2.insert(2)
h2.insert(11)


print('h2.array')
'''

# max heap stores smaller half values
# min heap stores larger half values
min_heap = Min_Heap([])
max_heap = Max_Heap([])

median_sum = 0

for i in input_data:
    if not max_heap.array:
        max_heap.insert(i)
        median_sum += i
        #print('max', max_heap.array)
        continue
        
    if i > max_heap.array[0]:
        min_heap.insert(i)
    else:
        max_heap.insert(i)
        
    # need to balance 2 heaps
    if len(min_heap.array) > len(max_heap.array) + 1:
        max_heap.insert(min_heap.pop())
    elif len(max_heap.array) > len(min_heap.array) + 1:
        min_heap.insert(max_heap.pop())
        
    if len(max_heap.array) >= len(min_heap.array):
        median_sum += max_heap.array[0]
        #print('median is', max_heap.array[0])
    else:
        median_sum += min_heap.array[0]
        #print('median is', min_heap.array[0])
        
    #print('max', max_heap.array)
    #print('min', min_heap.array)
    
print(median_sum % 10000)


# brute force solution

import statistics

median_total = 0
find_median_list = []

for i in input_data:
    find_median_list.append(i)
    median_total += statistics.median(find_median_list)

print(median_total % 10000)
# doesn't take too long either 




if __name__ == '__name__':
    # max heap stores smaller half values
    # min heap stores larger half values
    min_heap = Min_Heap([])
    max_heap = Max_Heap([])
    
    median_sum = 0
    
    for i in input_data:
        if not max_heap.array:
            max_heap.insert(i)
            median_sum += i
            #print('max', max_heap.array)
            continue
            
        if i > max_heap.array[0]:
            min_heap.insert(i)
        else:
            max_heap.insert(i)
            
        # need to balance 2 heaps
        if len(min_heap.array) > len(max_heap.array) + 1:
            max_heap.insert(min_heap.pop())
        elif len(max_heap.array) > len(min_heap.array) + 1:
            min_heap.insert(max_heap.pop())
            
        if len(max_heap.array) >= len(min_heap.array):
            median_sum += max_heap.array[0]
            #print('median is', max_heap.array[0])
        else:
            median_sum += min_heap.array[0]
            #print('median is', min_heap.array[0])
            
        #print('max', max_heap.array)
        #print('min', min_heap.array)
        
    print(median_sum % 10000)