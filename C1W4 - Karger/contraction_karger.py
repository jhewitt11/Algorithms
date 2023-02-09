import math
import random
import copy


def count_edges(network):
    count = 0
    for adj_l in network:
        count += len(adj_l)
    return int(count / 2)

def count_nodes(network):
    count = 0
    for node in network:
        if len(node) > 0:
            count += 1
    return count

def print_network(network):
    for count, adj_l in enumerate(network):
        if count != 0:
            print(adj_l)
    print("\n")

def pick_rand_edge(network):
    count = 0
    for adj_l in network:
        count += len(adj_l)  
    edge = random.randint(1, count)
    #print("\nedge count is ",edge)
    
    a_node = -1
    b_node = -1
    k = 1
    while b_node == -1:
        if edge > len(network[k]):
            edge -= len(network[k])
            k += 1
        else:
            a_node = k
            b_node = network[k][edge-1]
            #print("a_node is {}, b_node is {}\n".format(a_node, b_node)) 
    
    return a_node, b_node

def contract(network, a_node, b_node):
    
    network[a_node] += network[b_node]
    network[b_node] = []
    
    for adj_l in network:
        #adjust this to range
        for j, node in enumerate(adj_l):
            if node == b_node:
                adj_l[j] = a_node
        
    network[a_node][:] = [val for val in network[a_node] if val != a_node]
        
    
    return network



'''
og_network = []
with open('network.txt', 'r') as f:
    for line in f:
        line = line.split()
        
        adjacencies = []
        for count, value in enumerate(line):
            if count != 0:
                adjacencies.append(int(value))
        og_network.append(adjacencies)
    og_network.insert(0,[])

best = -1
for i in range(count_nodes(og_network)*10):
 
    network = copy.deepcopy(og_network)
    
    while count_nodes(network) > 2 :
        a_node, b_node = pick_rand_edge(network)
        network = contract(network, a_node, b_node)
    min_cut = count_edges(network)
    print("iter #{}\tmin cut is {}".format(i, min_cut))
    
    if best == -1 :
        best = min_cut
    if min_cut < best :
        best = min_cut

print("best min cut found is : {}".format(best))
'''