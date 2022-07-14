import heapq

lst = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(lst)

# get the largest k elements
print(heapq.nlargest(3, lst))

# get the smallest k elements
print(heapq.nsmallest(3, lst))

heapq.heappush(lst, 2)
heapq.heappush(lst, 12)

print(lst)


heapq.heappop(lst)
heapq.heappop(lst)

print(lst)

# pop first, then push
heapq.heapreplace(lst, 15)

# pop push, then pop
heapq.heappushpop(lst, 5)

# test workflow

# test branch
# test branch
