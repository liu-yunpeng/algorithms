import heapq

lst = [6, 7, 9, 4, 3, 5, 8, 10, 1]
  
# using heapify() to convert list into heap
heapq.heapify(lst)
  
# get the largest k elements
print(heapq.nlargest(3, lst))
  
# get the smallest k elements
print(heapq.nsmallest(3, lst))

heapq.heappush(lst,2)
heapq.heappush(lst,12)

print(lst)


heapq.heappop(lst)
heapq.heappop(lst)

print(lst)

# pop an item from the heap, then push the new item
heapq.heapreplace(heap, item)