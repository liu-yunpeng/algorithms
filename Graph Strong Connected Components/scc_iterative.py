from collections import defaultdict
import gc


input_file = r"input.txt"

print('started')

with open(input_file, 'r') as f:
    input_data = []
    for line in f:
        line = line.split()
        input_data.append([int(i) for i in line])

        
print('loading rev_graph')   
    
rev_input_data = []
for edge in input_data:
    rev_input_data.append([edge[1], edge[0]])

rev_graph = defaultdict(list)
for edge in rev_input_data:
    rev_graph[edge[0]].append(edge[1])    
    
del rev_input_data
gc.collect()


# 1st DFS_First loop, find finishing time in a revesed graph

seen_first = set()
finished_first = set()
finishing_time = 0

f_time_dict = {}    # {finishing_time: node}

for original_node in rev_graph.keys():
    if original_node not in seen_first:
        
        # iteratively traverse graph using depth first search
        first_call_stack = [original_node]
        while first_call_stack:
            node = first_call_stack.pop()
            if node not in seen_first:
                seen_first.add(node)
                first_call_stack.append(node)
                if node in rev_graph:
                    neighbors = rev_graph[node]
                    for n in neighbors:
                        if n not in seen_first:
                            first_call_stack.append(n)
            
            # there will be multiple paths to a node, so we need to track 
            # if we have seen this node in the finished set
            else:
                 if node not in finished_first:
                     finished_first.add(node)
                     finishing_time += 1
                     f_time_dict[finishing_time] = node

    
# memory management
del rev_graph
del seen_first
gc.collect()

print('loading graph' )
graph = defaultdict(list)
for edge in input_data:
    graph[edge[0]].append(edge[1])



# 2nd DFS_First loop, find leader in graph
seen_second = set()
finished_second = set()
leader = 0
leader_dict = defaultdict(list)


length = len(f_time_dict)

for i in range(length):
    #print(length - i, f_time_dict[length - i])
    from_node = f_time_dict[length - i]
    if from_node not in seen_second:
        leader = from_node
        
        # iteratively traverse graph
        second_call_stack = [from_node]
        while second_call_stack:
            node = second_call_stack.pop()
            if node not in seen_second:
                seen_second.add(node)
                second_call_stack.append(node)
                if node in graph:
                    neighbors = graph[node]
                    for n in neighbors:
                        if n not in seen_second:
                            second_call_stack.append(n)
                            
            # there will be multiple paths to a node, so we need to track 
            # if we have seen this node in the finished set
            if node not in finished_second:
                finished_second.add(node)
                leader_dict[leader].append(node)
            



#print(leader_dict)
scc = []
for i in leader_dict.keys():
    scc.append(len(leader_dict[i]))

scc.sort(reverse=True)
if len(scc) > 5:
    print(scc[:5])
else:
    print(scc)