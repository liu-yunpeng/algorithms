
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