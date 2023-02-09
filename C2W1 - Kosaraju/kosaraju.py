import math
import sys
import copy
from collections import Counter

def print_network(network):
    '''
    Print network.
    '''

    print("\ngraph :")
    for k, adj_l in enumerate(network):
        if k != 0:
            print(adj_l)
    print("\n")
    return

def invert_order(order):
    '''
    Swap indices and values.
    '''
    inv_order = [[] for x in range(len(order))]
    
    for k in range(len(order)):
        inv_order[order[k]] = k

    return inv_order

def compute_magic_order(rev_network):
    '''
    Depth First Search.
    
    Returns order of nodes visisted.
    '''

    n = len(rev_network)-1
    visited = [False] * (n+1)

    trail = []
    order = []

    for k in range(1, n+1):
        if visited[k] == False :
            visited[k] = True
            trail.append(k)
            
            while( len(trail) > 0):            
                cur = trail[-1]

                while((len(rev_network[cur]) > 0)):
                    cur = rev_network[cur].pop()
                    
                    if visited[cur] == True:
                        cur = trail[-1]
                    else :
                        trail.append(cur)
                        visited[cur] = True
                    
                order.append(cur)
                trail.pop()
    order.insert(0,0)
    
    return order

def remove_node(network, node):
    '''
    Remove node and connections in network.
    '''
    for adj_l in network:
        if node in adj_l:
            adj_l.remove(node)
    
    return network

def rearrange_to_magic(network, order):
    '''
    Rearrange network based on calculated order.
    '''
    magic_network = [[] for x in range(len(network))]
    
    for k in range(len(network)):
        adj_l = []
        for i in range(len(network[k])):
            adj_l.append(order[network[k][i]])
            
        magic_network[order[k]] = adj_l

    return magic_network

def network_reverse(network):
    '''
    Reverse connections in a network.
    '''
    rev_network = [[] for x in range(len(network))]
    
    for k in range(len(network)):  
        for node in network[k]:
            rev_network[node].append(k) 
    
    return rev_network

def compute_scc(m_network):
    '''
    Build strongly connected components (SCC) based on nodes found using Depth First Search.
    '''

    n = len(m_network)-1
    visited = [False] * (n+1)

    trail = []
    scc = []

    for k in range(n, 0, -1):
        if visited[k] == False :
            
            visited[k] = True
            trail.append(k)
            scc.append(k)
            
            while( len(trail) > 0):           
                cur = trail[-1]
                
                while((len(m_network[cur]) > 0)):
                    cur = m_network[cur].pop()
                    
                    if visited[cur] == True:
                        cur = trail[-1]
                    else:
                        scc.append(k)
                        trail.append(cur)
                        visited[cur] = True
                trail.pop()
    return scc

def top_scc_size(scc_l, num):
    '''
    Return top num largest strongly connected components in graph.
    '''
    
    top = []
    data = Counter(scc_l)
    
    if len(data) < num:
        print("Top {} SCCs requested, {} exist.".format(num, len(data.most_common())))
        num = len(data)
    
    sorted = data.most_common(num)
    
    for val, freq in sorted: 
        top.append(freq)
        
    return top

def read_in_network(DATA):
    '''
    Read in network from file.
    '''

    network = [[] for x in range(3)]
    max = len(network)-1
    
    with open(DATA, 'r') as f:
        for line in f:
            line = line.split()
            if len(line) == 2 :
                head = int(line[1])
                tail = int(line[0])

                if (head <= max) and (tail <= max):
                    network[tail].append(head)
                else:
                    if head > tail : 
                        new_max = head
                    else :
                        new_max = tail
                    addition = new_max - max
                    max = new_max
                    extension = [[] for x in range(addition)]
                    network = network + extension
                    network[tail].append(head)                  

    return network

G = [[],
            [5,2],
            [3,4],
            [1],
            [],
            [4,7],
            [5],
            [4,6]]
            
G2 = [[],
            [4],
            [8],
            [6],
            [7],
            [2],
            [9],
            [1],
            [6,5],
            [7,3]]

og_network = []

DATA = sys.argv[1]
TOP_NUM = int(sys.argv[2])

## read in adjacency list
## list [0] is empty so that node #1 can be addressed at [1]
'''
with open(DATA, 'r') as f:
    for line in f:
        line = line.split()
        adjacencies = []
        
        for count, value in enumerate(line):
            if count != 0:
                adjacencies.append(int(value))
                
        og_network.append(adjacencies)
    og_network.insert(0,[])
'''

network = read_in_network(DATA)
print("finished read in..")

#create the reversed network
network_reverse = network_reverse(network)
print("finished network reverse..")

#use DFS on reverse network to create magic order
order = compute_magic_order(network_reverse)
print("finished computing magic order..")

inv_order = invert_order(order)
print("finished inverting order..")

#rearrange original network with new node ordering from compute_magic_order
network_magic = rearrange_to_magic(network, inv_order)
print("finished rearranging network to magic network..")

#use DFS leader to calculate SCCs
scc = compute_scc(network_magic)
print("finished computing SCCs..")

#calculate top SCCs
top = top_scc_size(scc, TOP_NUM)
print("finished computing largest SCCs..")
print("Solution : ", top)
