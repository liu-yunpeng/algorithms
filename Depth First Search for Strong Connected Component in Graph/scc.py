from collections import defaultdict
import gc
from itertools import groupby

input_file = r"C:\Users\Yunpeng Liu\Documents\Stanford Online\Course 1 Divide and Conquer, Sorting and Searching, and Randomized Algorithms\assignment4.txt"
input_file = r"C:\Users\Yunpeng Liu\Documents\Stanford Online\Course 2 Graph Search, Shortest Paths, and Data Structures\assign 1 SCC\assignment1.txt"
#input_file = r"C:\Users\Yunpeng Liu\Documents\Stanford Online\Course 2 Graph Search, Shortest Paths, and Data Structures\assign 1 SCC\assignment1_test.txt"

print('started')

progress = 0

with open(input_file, 'r') as f:
    input_data = []
    for line in f:
        line = line.split()
        input_data.append([int(i) for i in line])
        progress += 1
        if progress % 10000 == 0:
            print('making progress {}'.format(progress))

        

    
rev_input_data = []
for edge in input_data:
    rev_input_data.append([edge[1], edge[0]])

rev_graph = defaultdict(list)
for edge in rev_input_data:
    rev_graph[edge[0]].append(edge[1])    
    
del rev_input_data
gc.collect()

#print(graph)
#print(rev_graph)

#print(graph)
#print(rev_graph)
print('loaded rev_graph')   

def DFS_First(graph, node):
    global finishing_time
    global f_time_dict
    global seen_first
    
    seen_first[node] = 1
    #print(node)
        
    if node in graph.keys():
        for neighbor in graph[node]:
            if neighbor not in seen_first:
                DFS_First(graph, neighbor)
            
    finishing_time += 1
    f_time_dict[finishing_time] = node
    
def DFS_Second(graph, node):
    global leader_dict
    global seen_second
    
    seen_second[node] = 1
    leader_dict[leader].append(node)
    
    if node in graph.keys():
        for neighbor in graph[node]:
            if neighbor not in seen_second:
                DFS_Second(graph, neighbor)
            



seen_first = {}
seen_second = {}
finishing_time = 0
leader = 0
leader_dict = defaultdict(list)
f_time_dict = {}    # {finishing_time: node}


progress = 0
# 1st DFS_First loop, find finishing time in a revesed graph
for node in rev_graph.keys():
    if node not in seen_first:
        seen_first[node] = 1
        DFS_First(rev_graph, node)
    
    if progress % 10000 == 0:
        print('first loop progress {}'.format(progress))
        
    progress += 1
    
#print(f_time_dict)
del rev_graph
del seen_first
gc.collect()

print('loaded graph' )
progress = 0
graph = defaultdict(list)
for edge in input_data:
    graph[edge[0]].append(edge[1])
    if progress % 10000 == 0:
        print('adj', progress)
        
    progress += 1


# 2nd DFS_First loop, find leader in graph
length = len(f_time_dict)
for i in range(length):
    #print(length - i, f_time_dict[length - i])
    from_node = f_time_dict[length - i]
    if from_node not in seen_second:
        leader = from_node
        seen_second[from_node] = 1
        DFS_Second(graph, from_node)

'''
for edge in graph:
    from_node, to_node = edge
    if from_node not in seen_second:
        seen_second[from_node] = 1
        leader = from_node
        print(leader)
        DFS_Second(graph, from_node)
'''

#print(leader_dict)
scc = []
for i in leader_dict.keys():
    scc.append(len(leader_dict[i]))

scc.sort()
print(scc)